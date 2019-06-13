def dict_count(a):
    if(a==[]):
        return "Your string is empty"
    else:
        dictA = {
            "a":0,
            "b":0,
            "z":0
        }
        dictA["a"] = a.count("a")
        dictA["b"]= a.count("b")
        dictA["z"] = a.count("z")

        total = dictA["a"]+dictA["b"]+dictA["z"]
        print("Total: "+str(total))
        ans = [(k,v) for k,v in dictA.items()]
        return ans

print(dict_count(["z", "z", "z", "z", "b", "b", "b", "b", "a", "a", "a", "a", "a", "a"]))
#print(dict_count([]))
