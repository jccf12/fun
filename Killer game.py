import random

n = int(input('insert number of players'))
names = []
for t in range(n):
    names.append(input("enter name"))


    
numbers = [i for i in range(n)]
random.shuffle(numbers)

done = False
while not done:
    for s in range(int(n/2)+1):
        if 2*s+1 < n:
            print(str(2*s)+". " + names[2*s] + '\t' + '\t' + '\t' + str(2*s+1)+". " + names[2*s+1])
        else:
            if n%2!=0:
                print(str(2*s)+'. ' + names[2*s])
        
    num = numbers.index(int(input('enter your number')))
    print(numbers[(num+1)%n])
    a = input("press enter when you're done")
    for y in range(70):
        print(' ')
    if a == "ok":
        done = True
    



