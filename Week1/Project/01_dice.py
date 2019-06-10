import random
print("Welcome to the dices game!")
n = input("Enter the number of dices you want to roll: ")
while(n.isdigit()==False or int(n)>8):
    print("USAGE: The number must be between 1 and 8")
    n = input("Enter the number of dices you want to roll: ")
num=int(n)
i=1
ans=0
if num==1:
    rad=random.randint(1,6)
    ans+=rad
else:
    while num>0:
        rad=random.randint(1,6)
        ans+=rad
        print("Dice "+str(i)+" : "+str(rad))
        i+=1
        num-=1
print("RESULT: "+str(ans))
