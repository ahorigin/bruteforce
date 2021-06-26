"""
P1 - > D3 D5 D7
P2 - > D3 D6 D7
P4 - > D5 D6 D7

1    0    1    0    1     1      0
D7  D6    D5   P4   D3    P2    P1
"""
4, 2, 0
4, 1, 0
2, 1, 0
class HammingCode():
    code = None
    type = None
    p1 = None
    p2 = None
    p4 = None
    error_index = None
    corrected_code = None
    hasError = False
    logs = []
    def __init__(self, code, type):
        self.code= code
        self.type = type
        self.p1_values()
        self.p2_values()
        self.p4_values()
        self.setError()

    def p1_values(self):
        alist =[self.code[6],self.code[4],self.code[2],self.code[0]]
        # print(alist)
        # print(alist.count("1"))
        if alist.count("1") % 2 == 0 and self.type=="1":
            self.p1 = "1"
            self.hasError = True
        else:
            self.p1 = "0"

    def p2_values(self):
        alist =[self.code[5],self.code[4],self.code[1],self.code[0]]
        # print(alist)
        # print(alist.count("1"))
        if alist.count("1") % 2 == 0 and self.type =="1":
            self.p2 = "1"
            self.hasError = True

        else:
            self.p2 = "0"
    def p4_values(self):
        alist =[self.code[3], self.code[2], self.code[1], self.code[0]]
        # print(alist)
        # print(alist.count("1"))
        if alist.count("1") % 2 == 0 and self.type=="1":
            self.p4 = "1"
            self.hasError = True
        else:
            self.p4 = "0"
    def setError(self):
        self.error_index = int("".join([self.p4,self.p2,self.p1]),2)
        # print(self.error_index)

    def correct_error(self):
        if self.hasError and self.error_index != 0:

            self.corrected_code = self.code
            baseTwo = int("".join([h.p4, h.p2, h.p1]), 2)
            current_bit = self.code[-baseTwo]
            if str(current_bit) == "1":
                listb = list(self.corrected_code)
                listb[-baseTwo] = "0"

                self.corrected_code = "".join(listb)
            else:
                listb = list(self.corrected_code)
                listb[-baseTwo] = "1"

                self.corrected_code= "".join(listb)
            return True
        return False

    def makeLog(self):
        ok = ""
        "D7 | D6 | D5 | P4 | D3 | P2 | P1"
        for bit in self.code:
            ok =" | ".join(list(self.code))
            """
            P1 - > D3 D5 D7
            P2 - > D3 D6 D7
            P4 - > D5 D6 D7

            1    0    1    0    1     1      0
            D7  D6    D5   P4   D3    P2    P1
            """

            p4 = [self.code[3], self.code[2], self.code[1], self.code[0]]
            p2 = [self.code[5], self.code[4], self.code[1], self.code[0]]
            p1 = [self.code[6], self.code[4], self.code[2], self.code[0]]
        p4_even = p4.count("1") % 2 == 0
        p2_even = p2.count("1") % 2 == 0
        p1_even = p1.count("1") % 2 == 0
        if self.type == "1":
            print("ODD PARITY")
        else:
            print("EVEN PARITY")

        p4_p =  None
        p2_p = None
        p1_p = None
        if self.type == "0":
            p4_p ="1"
            p2_p ="1"
            p1_p ="1"

            if p4_even:
                p4_p = "0"
            if p2_even:
                p2_p = "0"
            if p1_even:
                p1_p = "0"
        if self.type == "1":
            p4_p ="0"
            p2_p ="0"
            p1_p ="0"

            if p4_even:
                p4_p = "1"
            if p2_even:
                p2_p = "1"
            if p1_even:
                p1_p = "1"

        self.logs.append(f"P4 -> D5, D6, D7 = {p4} -> {p4.count('1')} ones -> Even ? {p4_even} -> P4 -> {p4_p}")
        self.logs.append(f"P2 -> D3, D6, D7 = {p2} -> {p2.count('1')} ones -> Even ? {p2_even} -> P2 -> {p2_p}")
        self.logs.append(f"P1 -> D3, D5, D7 = {p1} -> {p1.count('1')} ones -> Even ? {p1_even} -> P1 -> {p1_p}")
        self.logs.append("BINARY ->"+"".join([p4_p, p2_p, p1_p])+" DECIMAL -> "+str(int(str("".join([p4_p, p2_p, p1_p])),2))+" <- Error Position")
        # self.logs.append("Original -> "+self.code+ " Changed -> "+self.corrected_code)

#
# h = HammingCode("1010110",1)
# h.p1_values()
# h.p2_values()
# h.p4_values()


hamming_codes = ["10101101"
,"01010100"
,"10011011"
,"11011011"
,"10101110"
,"10100100"
,"10101011"
,"11011111"
,"00111011"
,"01011101"]


h = HammingCode("0011101","1")
if h.hasError:
    # print("poop")
    h.correct_error()

h.makeLog()
print("\n".join(h.logs))
#
# for code in hamming_codes:
#     h = HammingCode(code[:7],code[-1])
#     if h.hasError and h.error_index !=  0:
#         h.correct_error()
#         print("Original Code: " + code[:7] + " Corrected Code: " + h.corrected_code +" Error Bit: " + str(h.error_index))
#     else:
#         print("Original Code: "+code[:7]+ " has no error")
#
# # print("".join([h.p4,h.p2,h.p1]))
#
#
#         ok = ""
#         print("D7 | D6  | D5  | P4  | D3  | P2  | P1")
#
#             ok ="  |  ".join(list("0101110"))
#         # f"P4 -> D5, D6, D7 = [{self.code[3]}{self.code[2]},{self.code[3]},{self.code[0]}]"
#         # f"P2 -> D3, D6, D7 = [{self.code[5]},{self.code[4]},{self.code[1]},{self.code[0]}]"
#         # f"P1 -> D3, D5, D7 = [{self.code[6]},{self.code[4]},{self.code[2]},{self.code[0]}]"
