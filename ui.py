from PyQt5 import QtWidgets, uic, QtCore
import sys
import time

from PyQt5.QtCore import pyqtSignal, QThread, QObject, pyqtSlot
from PyQt5.QtWidgets import QFileDialog

import card_validator
import client_post
import hamming_code


class Ui(QtWidgets.QMainWindow):
    lower =  False
    number = False
    brute = False
    dictionary = False
    file = None
    letter_num = None
    evenParity = None
    oddParity = None

    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('untitled.ui', self) # Load the .ui file

        self.lc_chkbox.stateChanged.connect(self.lower_chkbox_onclick)
        self.num_chkbox.stateChanged.connect(self.num_chkbox_onclick)

        self.br_chkbox.stateChanged.connect(self.brute_chkbox_onlick)
        self.dc_chkbox.stateChanged.connect(self.dict_chkbox_onlick)

        self.select_btn.clicked.connect(self.openFile)
        self.select_lbl.setHidden(True)
        self.thread = QThread()

        self.start_btn.clicked.connect(self.startProcess)

        self.logTxtEdit.setReadOnly =True
        self.ltNumSbox.valueChanged.connect(self.spinValueChanged)

        self.end_btn.clicked.connect(self.end_process)

        ## related to the card thingy
        self.cardValidateBtn.clicked.connect(self.validate_card)
        self.validLbl.setHidden(True)
        self.invalidLbl.setHidden(True)

        ## related to the hamming code

        self.hammingCodeBtn.clicked.connect(self.check_hamming_code)
        self.evenRadioBtn.toggled.connect(self.evenRadioOnlick)
        self.oddRadioBtn.toggled.connect(self.oddRadioOnlick)
        self.errorLbl.setHidden(True)
        self.noErrorLbl.setHidden(True)


        # self.show() # Show the GUI
    def end_process(self):
        self.thread.terminate()

    def spinValueChanged(self):
        Ui.letter_num = self.ltNumSbox.value()
        # print(letter_num)
    def openFile(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        # dlg.setFilter("Text files (*.txt)")

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            if filenames is not None:
                Ui.file = filenames
                self.select_lbl.setHidden(False)
    # def updateText(self):
    #     self.logTxtEdit.appendPlainText("Hello")

    def startProcess(self):

        print(Ui.file)
        b=d=None
        if Ui.brute and Ui.dictionary:
            d = client_post.DictionaryAttack(Ui.file,self.url_txtbox.text())
            b = client_post.BruteForce(Ui.lower,Ui.number,Ui.letter_num,self.url_txtbox.text())
        elif Ui.brute and not Ui.dictionary:
            b = client_post.BruteForce(Ui.lower,Ui.number,Ui.letter_num,self.url_txtbox.text())

        elif not Ui.brute and Ui.dictionary:
            d = client_post.DictionaryAttack(Ui.file,self.url_txtbox.text())



        print(self.conn_lbl.text())
        # gen = b.generate()
        self.obj = Worker(b,d,self.txtPass.text())
        self.obj.intReady.connect(self.updateText)
        self.obj.moveToThread(self.thread)


        # self.obj.finished.connect(self.hide)  # To hide the progress bar after the progress is completed
        self.thread.started.connect(self.obj.proc_counter)
        self.thread.start()


    def updateText(self,value):
        # for b in value:
        self.logTxtEdit.appendPlainText(value)


    def brute_chkbox_onlick(self,state):
        if state == QtCore.Qt.Checked:
            Ui.brute = True
    def dict_chkbox_onlick(self,state):
        if state == QtCore.Qt.Checked:
            Ui.dictionary = True



    def lower_chkbox_onclick(self,state):
        if state == QtCore.Qt.Checked:
            Ui.lower = True

    def num_chkbox_onclick(self,state):
        if state == QtCore.Qt.Checked:
            Ui.number = True

    ## related to the card thingy
    def validate_card(self):
        self.logTxt.clear()
        self.validLbl.setHidden(True)
        self.invalidLbl.setHidden(True)
        v = card_validator.LuhmAlgorithm(self.cardNumTxt.text())
        if v.validate():
            self.validLbl.setHidden(False)
        else:
            self.invalidLbl.setHidden(False)
        self.logTxt.appendPlainText("\n".join(v.logs))

    ## hamming  code related
    def evenRadioOnlick(self):
        if self.evenRadioBtn.isChecked():
            self.evenParity =True
    def oddRadioOnlick(self):
        if self.evenRadioBtn.isChecked():
            self.oddParity   = True
    def check_hamming_code(self):
        self.hamLogTxt.clear()
        self.errorLbl.setHidden(True)
        self.noErrorLbl.setHidden(True)
        if self.evenParity:
            ham_obj = hamming_code.HammingCode(self.hammingCodeTxt.text(),"0")
        else:
            ham_obj = hamming_code.HammingCode(self.hammingCodeTxt.text(),"1")
        print(ham_obj.hasError)
        print(ham_obj.error_index)
        if ham_obj.hasError and ham_obj.error_index != 0:
            self.errorLbl.setHidden(False)
            ham_obj.correct_error()

            self.hamLogTxt.appendPlainText("\n".join(ham_obj.logs))
        else:
            self.noErrorLbl.setHidden(False)
        self.evenParity =False
        self.oddParity =False



class Worker(QObject):
    finished = pyqtSignal()
    intReady = pyqtSignal(str)
    objB = None
    objD = None
    batch = []
    password = None
    found= False
    def __init__(self, bObject,dObject,password):
        super().__init__()
        self.objB = bObject
        self.objD = dObject
        self.batch = []
        self.password = password

    @pyqtSlot()
    def proc_counter(self):  # A slot takes no params
        self.batch = []
        c = 0

        if Ui.brute and Ui.dictionary:
            self.dowork(self.objD)
            self.dowork(self.objB)
        elif Ui.brute and not Ui.dictionary:
            self.dowork(self.objB)

        elif not Ui.brute and Ui.dictionary:
            self.dowork(self.objD)

        self.finished.emit()

    def dowork(self,object):
        gen =  object.generate()
        c= 0
        for i in object.generate():
            c=c+1
            print(c,"out of ",object.combs)
            object.attack(i)
            if i == self.password:
                print(i)
                self.intReady.emit(i)
                self.found = True
                break
            else:
                self.intReady.emit(i)
                time.sleep(0.0001)

    def stop(self):
        self.terminate()




app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
app.exec_()