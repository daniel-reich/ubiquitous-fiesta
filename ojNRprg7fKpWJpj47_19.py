
def shift_sentence(txt):
    letters=[]
    fin=[]
    txt= txt.split(' ')
    for a in txt:
        letters.append(a[0])
    for a in reversed(range(0,len(letters)-1)):
        temp=letters[a+1]
        letters[a+1]=letters[a]
        letters[a]=temp
    for a in range(0,len(txt)):
        fin.append(letters[a]+txt[a][1:])
    fin=' '.join(fin)
    return fin

