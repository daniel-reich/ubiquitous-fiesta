
def clean_up(files, sort):
    
    a,b,c = [],[],[]
    if sort == "suffix":
        for i in files:
            a.append(i[(i.index(".")):])
        for i in a:
            if not i in b:
                b.append(i)
        for i in range(len(b)):
            k = str("c"+str(i))
            k= []
            c.append(k)
        for i in files:
            for j in b:
                if j == i[(i.index(".")):]:
                    c[b.index(j)].append(i)
        return (c)
​
    elif sort == "prefix":    
        for i in files:
            a.append(i[:(i.index("."))])
        for i in a:
            if not i in b:
                b.append(i)
        for i in range(len(b)):
            k = str("c"+str(i))
            k= []
            c.append(k)
        for i in files:
            for j in b:
                if j == i[:(i.index("."))]:
                    c[b.index(j)].append(i)
        return (c)

