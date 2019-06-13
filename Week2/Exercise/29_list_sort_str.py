def list_sort_str(a):
    ans = []
    for i in a:
        if i.isdigit()==False:
            ans.append(i)
    ans.sort()
    return ans

print(list_sort_str(["abc", "4", "2", "3", "dza", "def"]))
            
