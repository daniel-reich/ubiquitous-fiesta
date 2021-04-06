
def count_same_ends(txt):
    txt = txt.lower().replace('!',"").replace('.',"").split(' ')
    m=0
    for w in txt:
        if w[0]==w[-1] and len(w)!=1:m+=1
    return m

