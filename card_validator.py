"""
How the Luhn Algorithm Works
The LUHN formula algorithm was developed by a German Computer Scientist
 named Hans Peter Luhn in 1954 while working as a researcher at IBM.
  The exact workings of the algorithm are based on modular
 arithmetic, a mathematical technique developed by Carl Friedrich
  Gauss in the early 19th century. Although its detailed workings are
  rather complex, it is best known for allowing computers to quickly
   assess whether the credit card numbers provided by customers are accurate.
"""
import math


class LuhmAlgorithm:
    card_num = None
    logs = []
    def __init__(self, card_num):
        self.card_num = card_num
        self.logs = []
    def validate(self):
        # print(self.card_num)
        sum = 0
        for i in range(2,len(self.card_num)+1,2):
            # doubling the number
            doubled = int(self.card_num[-i])*2
            # self.logs.append(str("Value: "+str(self.card_num[-i])+" Doubled: "+str(int(self.card_num[-i])*2)))
            if len(str(doubled)) > 1:
                self.logs.append(str("Value: "+str(doubled)+" Added: "+str(int(str(doubled)[0])+int(str(doubled)[1]))))
                doubled = int(str(doubled)[0])+int(str(doubled)[1])

            else:
                self.logs.append(
                    str("Value: " + str(self.card_num[-i]) + " Doubled: " + str(int(self.card_num[-i]) * 2)))

            # print("sum: ",sum)
            sum = sum+doubled
        # nop= [int(self.card_num[-i]) for i in range(2, len(self.card_num)+1, 2)]
        other =  [int(self.card_num[-k]) for k in range(1,len(self.card_num),2)]
        # print(nop)
        # print(other)
        # print(math.fsum(other))

        print(self.logs)
        self.logs.append(str("Sum of not second digits:"+str(math.fsum(other))))
        self.logs.append(str("Sum of every second digits:"+str(sum)))
        sum = math.fsum(other) + sum
        self.logs.append("Modulo Operation: "+str(sum)+" % "+"10"+" = "+str(sum % 10))
        print("\n".join(self.logs))

        return  sum % 10 == 0

        # for c in reversed(self.card_num):
        #     print(c)

la = LuhmAlgorithm("5264310242749474")
print(la.validate())
card_num = "5264310242749474"

5+9+5+8+0+3+8+8