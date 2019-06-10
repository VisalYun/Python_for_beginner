import random
name = input("Hello, what is your name? ")
play="Y"
while play=="Y":
    print("Well "+name+", try to guess the number I have in mind!")
    count=0
    gen_num = random.randint(1,100)
    mag_num = int(input())
    while mag_num!=gen_num:
        if mag_num>gen_num/2:
            print("Too high, try again!")
        elif mag_num<gen_num/2:
            print("Too low, try again!")
        count+=1
        mag_num = int(input())
    print("It took you "+str(count)+" turns to guess my number which was "+str(mag_num)+"!")
    play = input("Do you want to play again? [Y/N] ")
    while play != "Y" and play != "N":
        print("Sorry, I did not understand. Let me repeat: ")
        play = input("Do you want to play again? [Y/N] ")
    if(play == "N"):
        break
    else:
        print("==========")
print("Ok, bye "+name+"! See you later!")