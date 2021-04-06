
def validate_swaps(lst, txt):
    import itertools
    changes=list(itertools.combinations(range(len(txt)),2))
    wordlist=[]
    for change in changes:
        text=list(txt[:])        
        text[change[0]]=txt[change[1]]
        text[change[1]]=txt[change[0]]
        wordlist.append("".join(text))
    res=[]
    for word in lst:
        if word in wordlist:
            res.append(True)
        else:
            res.append(False)
    return res

