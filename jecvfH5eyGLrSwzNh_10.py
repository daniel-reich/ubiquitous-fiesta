
def fauna_number(txt):
    animals = ["muggercrocodile", "one-hornedrhino", "python", "moth", "monitorlizard", "bengaltiger"]
    txt=txt.replace(',',' ').split()
    lst=[]
    y=[]
    for i in txt:
        if i in animals:
            lst.append(i)
        if i.isnumeric():
            y.append(i)
    if len(lst)==0:
        return lst
    if len(lst)==1:
        return [(lst[0],y[0])]
    else:
        return [(lst[0],y[0]),(lst[1],y[1])]

