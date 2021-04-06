
def recur_index(txt,p=0, lst=None, sol=None):
    if not lst: lst, sol = [], []
    if txt:
        if txt[0] not in lst: lst+= [txt[0], p]
        else: return {txt[0]:[lst[lst.index(txt[0])+1],p]}
    return recur_index(txt[1:],p+1, lst, sol) if txt else {}

