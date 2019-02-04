import random
import tester

## creates list of words for difficulty setting
f = open('20k.txt', 'r')
list = []
list4 = []
list7 = []
list10 = []
for word in f.read().split():
    if len(word) == 4:
        list4.append(word)
    elif len(word) == 7:
        list7.append(word)
    elif len(word) == 10:
        list10.append(word)

## user selects difficulty
tries = 0
diff = 0
secretWord = ""
while tries < 10:
    try:  
        diff = int(input("Please select difficulty level. 1: easy 2: medium 3: hard "))
        break
    except ValueError:
        print("enter 1 2 or 3")
        tries += 1

## decides which of the lists/which script to use

if diff == 1:
    randNum = random.randint(0, len(list4))
    secretWord = list4[randNum]
    tester.easy(secretWord)
elif diff == 2:
    randNum = random.randint(0, len(list7))
    secretWord = list7[randNum]
    tester.medium(secretWord)
else:
    randNum = random.randint(0, len(list10))
    secretWord = list10[randNum]
    tester.hard(secretWord)
