
def duplicates(lst, item):
    return [i for i, x in enumerate(lst) if x == item]

def easy(tester):
    temp2 = []
    temp3 = ["_"]*len(tester)
    for chars in tester:
        temp2.append(chars)
    counter = 8
    temp = "____"
    
    while counter > 0:
        try:
            guess = input("guess a letter. ")
            if len(guess) > 1:
                raise ValueError
            counter -= 1
            if guess in temp2:
                ind = duplicates(temp2, guess)
                for nums in ind:
                    temp3[nums] = guess

                temp4 = ''.join(temp3)
                print("good guess. %d guesses left " % counter)
                print(temp4)
                if temp4 == tester:
                    print("you win!")
                    exit()

                
            else:
                print("incorrect %d guesses left" % counter)
                

        except ValueError:
            print("1 letter at a time")
        if counter == 0:
            print("you lose.")
            print(tester)
            exit()
            

    
    


def medium(tester):
    temp2 = []
    temp3 = ["_"]*len(tester)
    for chars in tester:
        temp2.append(chars)
    counter = 12
    temp = "____"
    
    while counter > 0:
        try:
            guess = input("guess a letter. ")
            if len(guess) > 1:
                raise ValueError
            counter -= 1
            if guess in temp2:
                ind = duplicates(temp2, guess)
                for nums in ind:
                    temp3[nums] = guess

                temp4 = ''.join(temp3)
                print("good guess. %d guesses left" % counter)
                print(temp4)
                if temp4 == tester:
                    print("you win!")
                    exit()

                
            else:
                print("incorrect %d guesses left" % counter)
                

        except ValueError:
            print("1 letter at a time ")
        if counter == 0:
            print("you lose.")
            print(tester)
            exit()
            


def hard(tester):
    temp2 = []
    temp3 = ["_"]*len(tester)
    for chars in tester:
        temp2.append(chars)
    counter = 15
    temp = "____"
    
    while counter > 0:
        try:
            guess = input("guess a letter. ")
            if len(guess) > 1:
                raise ValueError
            counter -= 1
            if guess in temp2:
                ind = duplicates(temp2, guess)
                for nums in ind:
                    temp3[nums] = guess

                temp4 = ''.join(temp3)
                print("good guess. %d guesses left" % counter)
                print(temp4)
                if temp4 == tester:
                    print("you win!")
                    exit()

                
            else:
                print("incorrect %d guesses left" % counter)
                

        except ValueError:
            print("1 letter at a time ")
        if counter == 0:
            print("you lose.")
            print(tester)
            exit()
            
