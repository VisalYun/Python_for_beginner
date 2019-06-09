l=[]
while True:
    s = input("Enter a string: ")
    if(s=="Generate"):
        break;
    else:
        l.append(s)
n=0
while n< len(l):
    print("<p>"+l[n]+"</p>")
    n+=1
