import random
num=random.randint(1,10000)
count=0
while (1):
    x=int(input("ENTER THE NUMBER : "))
    if(x==num):
        print("YOU GOT THE ANSWER")
        count+=1
        print(f" {count} number of attempts")
    else:
        print("MISSMATCH")
