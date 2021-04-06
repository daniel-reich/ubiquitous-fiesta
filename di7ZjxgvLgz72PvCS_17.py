
def swap(strg,i1,i2):
    strlist = []
    for char in strg: 
        strlist.append(char) 
    temp = strlist[i1]
    strlist[i1] = strlist[i2]
    strlist[i2] = temp
    joined = "".join(strlist)
    return joined 
​
def validate_swaps(lst, txt):
    boolst = []
    word = "No!"
    for strg in lst: 
        word = "No!"
        for i in range(len(strg)): 
            for j in range(i+1,len(strg)):
                swappedstr = ""
                if i != j: 
                    swappedstr = swap(strg,i,j)
                if swappedstr == txt: 
                    boolst.append(True)
                    word ="Yes!"
                    break
            if word == "Yes!":
                break 
        if word == "No!":
            boolst.append(False) 
    return boolst

