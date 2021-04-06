
def all_about_strings(txt):
    L, FC,LC = len(txt), txt[0],txt[-1] #len, first, second
    #Midle
    if len(txt)%2==1:
        M = txt[len(txt)//2]
    else:
        M= txt[(len(txt)//2)-1:(len(txt)//2)+1]    
    return [L,FC,LC,M,second(txt)]
    
def second(X):
    N = list(enumerate(X))
    L =[]
    for inx,s in N:
        if s==X[1]:
            L.append(inx)
    if len(L)>=2:
        return '@ index {}'.format(L[-1])
    else:
        return "not found"

