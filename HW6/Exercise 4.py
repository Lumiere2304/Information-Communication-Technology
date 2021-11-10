# Exercise 4
def isWordPresent (sentence,word):
    text = sentence.split(" ")
    for i in text:
        if (i == word):
            return True
        return False
text = input()
word = input()
if (isWordPresent(text, word)):
    print(True)
else:
    print(False)