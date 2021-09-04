import mysql.connector
import difflib

con = mysql.connector.connect(
    user = 'ardit700_student',
    password = 'ardit700_student',
    host = '108.167.140.122',
    database = 'ardit700_pm1database'
)

cursor = con.cursor()

word = input("Enter a word: ")
word = word.lower()

def findWord(word):
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'"%word)
    results = cursor.fetchall()

    if results:
        return results
    else:
        query = cursor.execute("SELECT DISTINCT Expression FROM Dictionary")
        results = cursor.fetchall()

        lst = [ results[i][0] for i in range(len(results))]
        bitch = difflib.get_close_matches(word, lst)
        if bitch[0]:
            ch = input("Did you mean '%s'? [Y/N]: "%bitch[0])
            if ch == 'y' or ch == 'Y':
                return findWord(bitch[0])
        if bitch[1]:
            ch = input("Did you mean '%s'? [Y/N]: "%bitch[1])
            if ch == 'y' or ch == 'Y':
                return findWord(bitch[1])
        return []

results = findWord(word)
if results:
    for item in results:
        print("> ", item[1])
else:
    print("Word not found!")











# import json
# import difflib

# data = json.load(open('data.json'))
# str = input("\nEnter a word: ")

# print("\b", end='')
# def findWord(w):
#     w = w.lower()
#     if w in data.keys():
#         return data[w]

#     else:
#         lst = difflib.get_close_matches(w, data.keys())
#         for j in lst:
#             ch = input("Did you mean '"+ j +"' [Y/N]:")
#             if ch == 'y' or ch == 'Y':
#                 return data[j]
#         return ["!!! Word doesn't exist! Please double check it. !!!"]

# print("\n")
# for i in findWord(str):
#     print("> ",i)
