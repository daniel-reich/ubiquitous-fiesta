
def sock_pairs(pair):
    mydict = {}
    count = 0
    
    for i in range (len(pair)):
        if pair[i] not in mydict:    
             mydict[pair[i]] = 1
        else:
             mydict[pair[i]] += 1
    for keys,values in mydict.items():
        count += int(values/2)
    return count

