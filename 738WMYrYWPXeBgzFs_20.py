
def is_valid(txt):
    mydict = {}
    for i in txt:
        if i in mydict:
            mydict[i] += 1
        else:
            mydict[i] = 1
    print(mydict)
    
    values = []
    for i in mydict:
        #print(mydict[i])
        values.append(mydict[i])
    values.sort()
    for i in range(len(values)-1):
        print(i)
        if values[i] == values[-1] and len(list(set(values)))!= 1 or (values[-1]-values[0])>1:
            return "NO"
    return "YES"

