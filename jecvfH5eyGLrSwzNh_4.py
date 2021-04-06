
def fauna_number(txt):
    animals = ["muggercrocodile","one-hornedrhino",
               "python","moth","monitorlizard","bengaltiger"]
​
    txt = txt.replace(',',' ')
    txt = txt.replace('.',' ')
    lst = txt.split()
    res = []
    for item in lst:
        if(item in animals):
            try:
                ind = lst.index(item)
                print('IND', ind)
                if(ind >= 0):
                   res.append((lst[ind], lst[ind - 1]))
            except:
                pass
​
    return res

