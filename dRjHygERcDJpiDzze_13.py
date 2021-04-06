
def lengthen(txt, r):    
    short, lng = sorted([r, txt], key=len)
    return (short * len(lng))[:len(lng)]

