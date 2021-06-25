# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import simplejson
import cgi

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org"
                               "<body>/body>"
                               "</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><form type='POST' action ='/'><input name='password   '></input><button "
                               "type='submit'>Click</button></form><", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_POST(self):
        self._set_headers()
        print ("in post method")
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        self.send_response(200)
        self.end_headers()
        print(self.data_string.decode("ascii"))
        if self.data_string.decode("ascii").split("=")[1] == "aa":
            self._set_response()
            self.wfile.write("SUCCESS".encode('utf-8'))
            # self.do_GET()

            # print("access grant")
        # print(self.data_string.decode("ascii").split("=")[1])
        # data = simplejson.loads(self.data_string.decode("ascii"))



if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
# #
import itertools
import random
# #
# #     # for comb in itertools.permuations(
# #     #         ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
# #     #          "v", "w", "x", "y", "z","1","2","3","4","5","6","7","8","9","0"], 3):
# #     #     # if "".join(comb) == "bom":
# #     #     print("".join(comb))
# #     #         # break
#
# # for comb in itertools.permutations(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
# #              "v", "w", "x", "y", "z","1","2","3","4","5","6","7","8","9","0"], 6):
# #     # if "".join(comb) == "alihas":
# #     print("".join(comb))
# done = []
#
# from datetime import datetime
# start=datetime.now()
#
# first_letters  = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
#              "v", "w", "x", "y", "z","1","2","3","4","5","6","7","8","9","0"]
# #
# for var in range(len(first_letters)):
#     first_random_letter = first_letters[random.randint(0,len(first_letters)-1)]
#     if first_random_letter not in done:
#         print(first_random_letter)
#         copy_first = first_letters.copy()
#         copy_first[0] = first_letters[first_letters.index(first_random_letter)]
#         copy_first[first_letters.index(first_random_letter)] ="a"
#         for comb in itertools.product(copy_first,repeat=6):
#             print("".join(comb))

#     done.append(first_random_letter)
# #
# # print(datetime.now()-start)
# #
#
#
# def password_generator(letters, length):
#     first_random_letter = first_letters[random.randint(0,len(first_letters)-1)]
#     if first_random_letter not in done:
#         # print(first_random_letter)
#         copy_first = first_letters.copy()
#         copy_first[0] = first_letters[first_letters.index(first_random_letter)]
#         copy_first[first_letters.index(first_random_letter)] ="a"
#         for comb in itertools.product(copy_first,repeat=length):
#             return "".join(comb)
#
# for var in range(len(first_letters)):
#     print(password_generator(first_letters,3))
