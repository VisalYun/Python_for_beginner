ans = 0
while True:
    n = input("Enter a number: ")
    if(n.isdigit()==True):
        num=int(n)
        ans+=num
        print("TOTAL: "+ str(ans))
    elif(n=="exit"):
        exit(1)
    else:
        print("TOTAL: "+ str(ans))
