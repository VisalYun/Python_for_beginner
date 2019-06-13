def dict_count(a):
    ansDict = {
        "a":0,
        "b":0,
        "c":0,
        "d":0,
        "e":0
    }
    ansDict["a"] = a.count("a")
    ansDict["b"] = a.count("b")
    ansDict["c"] = a.count("c")
    ansDict["d"] = a.count("d")
    ansDict["e"] = a.count("e")
    return ansDict;

print(dict_count(["a", "a", "a", "b", "c", "d", "c", "b", "c", "d", "c", "e", "e", "e"]))
            
