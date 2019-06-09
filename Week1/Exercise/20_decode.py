s = input("Enter your encrypted message: ")
i=0
ans=""
if s == "":
    print("Nothing to encode.")
else:
    while i<len(s):
        n=ord(s[i])
        if(n>=65 and n<=90):
            n-=13
            if(n<65):
                n=90-(65-n-1)
            ans+=chr(n)
        elif(n>=97 and n<=122):
            n-=13
            if(n<97):
                n=122-(97-n-1)
            ans+=chr(n)
        else:
            ans+=s[i]
        i+=1
print(ans)
