def list_sort_int(a):
    ans=[]
    for i in a:
        if i.isdigit()==True:
          ans.append(int(i))
    ans.sort()
    return set(ans)

print(list_sort_int(["abc", "4", "4", "4", "4", "2", "3", "dza", "def"]))
