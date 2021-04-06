
def remix(txt,lst):
    d=dict(zip(lst,txt))
    ls=[]
    for a in d:
        ls.insert(a,d[a])
    return ''.join(ls)

