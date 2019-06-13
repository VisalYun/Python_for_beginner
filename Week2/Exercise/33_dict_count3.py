def dict_count(a):
    if(a==[]):
        return "Your string is empty"
    else:
        dictA = {
            "a":0,
            "b":0,
            "c":0,
            "d":0,
            "e":0
        }
        dictA["a"] = a.count("a")
        dictA["b"]= a.count("b")
        dictA["c"] = a.count("c")
        dictA["d"] = a.count("d")
        dictA["e"] = a.count("e")

        total = dictA["a"]+dictA["b"]+dictA["c"]+dictA["d"]+dictA["e"]
        print("Total: "+str(total))
        ans = [(k,v) for k,v in dictA.items()]
        return ans

print(dict_count(["a", "b", "b", "c", "c", "c", "c", "d", "d", "e", "e", "e"]))
#print(dict_count([]))
