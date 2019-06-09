s = input("Enter a string: ")
i=0
ans=""
while i<len(s):
    n=ord(s[i])
    if(n>=65 and n<=90):
        ans+=s[i].lower()
    elif(n>=97 and n<=122):
        ans+=s[i].upper()   
    i+=1
print(ans)
