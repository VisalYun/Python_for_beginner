import re
import operator
def top_words(s):
    if s == "":
        return []
    else:
        word_list = s.split()

        temp=[]
        empty=""
        for i in range(len(word_list)):
            empty=" ".join(re.sub("[^a-z'A-Z]","",word_list[i]))
            temp.append(empty.replace(" ","").lower())

        temp_dict={}
        for i in range(len(temp)): 
            temp_dict[temp[i]] = temp.count(temp[i])
        temp_dict = sorted(temp_dict.items(), key = lambda x:x[1], reverse=True)
        
        ans = []
        ans = [x for x, val in temp_dict]
        if ans[0]=="":
                return []
        else:
            return ans[0:3:1]

print(top_words("Welcome to Kirirom: Kirirom Institute of Technology and Kirirom National Parc. To contact us, send a message to us!"))
print(top_words("//can't cant Cant can't"))
print(top_words("“hi hello hi wow wow hello good good"))
print(top_words(". ??? // ####### // // ???"))
print(top_words(""))