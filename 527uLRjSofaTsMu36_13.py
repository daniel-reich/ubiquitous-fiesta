
def get_middle(txt):
    if len(txt) == 0 :
        return txt
    
    if len(txt) % 2 == 0:
        return txt[int(len(txt)/2) -1] + txt[int((len(txt)/2))]
    elif len(txt) % 2 == 1:
        return txt[int(len(txt)//2)]

