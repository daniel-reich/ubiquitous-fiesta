
def tweet(txt):
    c=[]
    a= ''.join(i for i in txt if i not in ['.',',','!','?'])
    for i in a.split():
        if '#' in i:
            c.append(i)
        elif '@' in i:
            c.append(i)
    return ' '.join(c)

