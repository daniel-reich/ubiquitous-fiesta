
def vertical_txt(txt):
    tmp=txt.split(" ")
    l=len(max(tmp,key=len))
    lst=[x+"".join([" "]*(l-len(x))) for x in tmp]
    x=zip(*lst)
    lst1=[list(y) for y in x]
    return lst1

