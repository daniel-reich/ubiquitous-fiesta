
def num_to_eng(n):
    eng=['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen',\
         'fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','','','twenty','thirty','forty','fifty',\
         'sixty','seventy','eighty','ninety']
    d=e=f=g=0
    s=''
    d=n%100
    e=n//100
    f=d%10
    g=d//10
    if e:
        s+=eng[e]+' '+'hundred '
    if g>1:
        s+=eng[g+20]+' '+eng[f]
    else:
        s+=eng[d]
    if s=='':
        s='zero'
    return s

