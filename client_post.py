import requests, random, itertools

ENDPOINT = "http://localhost:8080/"

first_letters  = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v", "w", "x", "y", "z","1","2","3","4","5","6","7","8","9","0"]
done = []
for var in range(len(first_letters)):
    first_random_letter = first_letters[random.randint(0,len(first_letters)-1)]
# first_random_letter ="h"
    if first_random_letter not in done:
        print(first_random_letter)
        copy_first = first_letters.copy()
        copy_first[0] = first_letters[first_letters.index(first_random_letter)]
        copy_first[first_letters.index(first_random_letter)] ="a"
        for comb in itertools.product(copy_first,repeat=2):
            data = {'password': "".join(comb)}
            r = requests.post(url=ENDPOINT, data=data)
            if r.content.decode("ascii").split("\n")[-1] == "SUCCESS":
                print("done")
                break
        # print(r.)
        # r.


# defining the api-endpoint
# data to be sent to api


# sending post request and saving response as response object

# # extracting response text
# pastebin_url = r.text
# print("The pastebin URL is:%s" % pastebin_url)