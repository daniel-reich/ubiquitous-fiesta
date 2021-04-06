
def sorting(txt):
    a=sorted([i.lower() for i in txt if i.isalpha()])
    c=sorted([i for i in txt if i.isnumeric()])
    d=[]
    for i in a:
        if i not in d:
            if i in txt:
                d.append(i)
                if i.upper() in txt:
                    d.append(i.upper())
            elif i.upper() in txt :
                d.append(i.upper())
    d.extend(c)
    return "".join(d)

