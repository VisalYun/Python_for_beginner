n = input("Enter a number: ")
if(n=="EXIT" or n=="exit"):
    exit(1)
elif(n.isdigit()==True):
    num = int(n)
    if(num%2==0):
        print(n +" is EVEN")
    else:
        print(n +" is ODD")
else:
    print(n+" is not a valid number.")
