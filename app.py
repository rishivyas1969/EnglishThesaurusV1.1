import json
import difflib

data = json.load(open('data.json'))
str = input("\nEnter a word: ")

def findWord(w):
    w = w.lower()
    print(w)
    if w in data.keys():
        return data[w]
    else:
        return ["!!! Word doesn't exist! Please double check it. !!!"]

print("\n")
for i in findWord(str):
    print("> ",i)
