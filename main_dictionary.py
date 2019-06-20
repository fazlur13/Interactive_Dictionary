import json
#import difflib #Library used to compare text
#from difflib import SequenceMatcher #SequenceMatcher is a method in difflib use for compare to text block
from difflib import get_close_matches  #Retuen the most similar matches having match ratio greater then .6
data=json.load(open("data.json"))

def translate(w):
    w=w.lower()  #To convert the entered word into loweer case
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no" %get_close_matches(w, data.keys())[0]).upper()
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist, please check dounle check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist, please check dounle check it."
word = input("Enter a word:")

#print(translate(word))   #This will print list view.
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)