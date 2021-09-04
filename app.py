import json
import difflib

data = json.load(open('data.json'))
str = input("\nEnter a word: ")

print("\b", end='')
def findWord(w):
    w = w.lower()
    if w in data.keys():
        return data[w]

    else:
        lst = difflib.get_close_matches(w, data.keys())
        for j in lst:
            ch = input("Did you mean '"+ j +"' [Y/N]:")
            if ch == 'y' or ch == 'Y':
                return data[j]
        return ["!!! Word doesn't exist! Please double check it. !!!"]

print("\n")
for i in findWord(str):
    print("> ",i)
