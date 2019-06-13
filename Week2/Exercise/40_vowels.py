import re
def vowels(a):
    temp = re.sub("[^a-z]","",a)
    count=0
    v=""
    nv=""
    i=0
    while i< len(a):
        if a[i:i+1]=="a" or a[i:i+1]=="e" or a[i:i+1]=="i" or a[i:i+1]=="o" or a[i:i+1]=="u":
            count+=1
            v+=a[i:i+1]
        i+=1
    nv=re.sub("[aeiou]","",temp)
    print(count)
    print(v)
    print(nv.upper())

vowels("what is that ?")
