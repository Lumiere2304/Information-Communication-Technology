# Exercise 1
s1 = input()
i = int(input())
print(s1.replace(s1[i], "", 1))

# Exercise 2
s2 = list(input().split(" "))
for W in s2:
    if (len(W) % 2 == 0):
        print(W)

# Exercise 3
s3 = input()
print(len(s3))

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

# Exercise 5
s5 = input().replace(".", ",")
print("Number of commas is", s5.count(","))
