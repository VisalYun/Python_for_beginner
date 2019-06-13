def acronym(a):
    if a == []:
        return a
    else:
        ans=[]
        for i in a:
            ans.append(i[0:1].upper())
        return ans

print(acronym(["world", "wide", "web"]))
print(acronym([]))
        
