## returns index of item if it is in the word
def duplicates(lst, item):
    return [i for i, x in enumerate(lst) if x == item]

def game(tester, mode):
    counter = 7
    temp2 = []
    temp3 = ["_"]*len(tester)
    for chars in tester: ## splits string into a list 
        temp2.append(chars)
    
    while counter > 0:
        try:
            guess = input("guess a letter. ")
            if len(guess) > 1: ## makes sure user only enters 1 letter at a time
                raise ValueError
            if guess in temp2:
                ind = duplicates(temp2, guess)
                for nums in ind: ##replacing "_" with the correct letter
                    temp3[nums] = guess

                temp4 = ''.join(temp3) ## converting list back to a string 
                print("good guess. %d guesses left " % counter)
                print(temp4)
                if temp4 == tester:
                    print("you win!")
                    exit()

                
            else:
                counter -= 1
                print("incorrect %d guesses left" % counter)
                

        except ValueError:
            print("1 letter at a time")
        if counter == 0: ## user runs out of guesses
            print("you lose.") 
            print(tester)
            exit()