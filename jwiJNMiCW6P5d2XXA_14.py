
def does_rhyme(txt1, txt2):
    a= txt1.split(" ")
    b= txt2.split(" ")
    print(a,b)
    vowels= {'a':0,'e':0,'i':0,'o':0,'u':0}
​
    for items in a[-1]:
        if items.lower() in vowels.keys():
            vowels[items.lower()]+=1
​
    for items in b[-1]:
        if items.lower() in vowels.keys():
            if vowels[items.lower()]==0:
                return False
            else:
                vowels[items.lower()]-=1
​
​
    for k,v in vowels.items():
        if v>0:
            return False
​
    return True

