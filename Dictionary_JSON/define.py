import json
from difflib import get_close_matches

"""
Dictionary_JSON: define.py, dictonary.json

Loads a JSON to find a definition for a users word. If the user slightly mistypes the word or is close 
it will try to identify the next best thing by using an imported library get_close_matches. 
 
"""


data = json.load(open("dictonary.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        correctInput = input("Did you mean %s instead?: " % get_close_matches(w, data.keys())[0])
        while True:
            correctInput = correctInput.lower()
            if correctInput == 'y' or correctInput == "yes":
                return data[get_close_matches(w, data.keys())[0]]
            elif correctInput == 'n' or correctInput == 'no':
                return "The word doesn't exist in our \"dictonary.json\"."
            else:
                correctInput = input("Please respond in Y or N: ")
    else:
        return "The word doesn't exist in our \"dictonary.json\"."


word = input("Enter word: ")

output = translate(word)
if type(output) == list:
    for i in range(len(output)):
        print("%d. " % (i+1) + "%s" % output[i])
else:
    print(output)