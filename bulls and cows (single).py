import random


def game():
    

    numOfDig = int(input("enter number of digits"))
    
    secretnumber = ''
    for i in range(numOfDig):
        if i == 0:
            x = str(random.randrange(1,10))
        else:
            x = str(random.randrange(10))
        while x in secretnumber:
            if i == 0:
                x = str(random.randrange(1,10))
            else:
                x = str(random.randrange(10))
                
        secretnumber = secretnumber + x

    guess = input("Enter guess")
    b = 0
    c = 0
    tries = 1
    while guess != secretnumber:
        
        b = 0
        c = 0
        for i in range(numOfDig):
            if guess[i] == secretnumber[i]:
                b = b + 1
        for i in range(numOfDig):
            if guess[i] in secretnumber:
                c = c + 1
        c = c - b
        print("bulls: ", b, "cows: ", c)
        guess = input("Enter new guess")
        tries = tries + 1
    

    print("Congratulations you have guessed the number in ", tries, " tries")
    answer = input("Do you want to play again?")
    if answer == "yes":
        finished = False
    if answer == "no":
        finished = True

    return finished

finished = False

while not finished:
    finished = game()
        
    
    
