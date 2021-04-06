
def split_n_cases(txt, cases):
    s = len(txt)//cases
    return ["Error"] if len(txt)%cases!=0 else [txt[i:i+s] for i in range(0, len(txt), s)]

