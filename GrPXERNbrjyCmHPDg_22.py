
def duplicate_count(txt):
    newcount = 0
    new = str(txt)
    se = set(new)
    l= []
    for i in se:
        sub = str(i)
        #print(sub)
        count = new.count(sub)
        #print('count',count)
        if count>=2:
            newcount += 1
            #print('newcount',newcount)
            l.append(newcount)
        #print(l)
    return newcount

