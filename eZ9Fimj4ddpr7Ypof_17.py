
def mumbling(s):
    res =[]
    for i,v in enumerate(list(s)):
        res.append((v.lower()*(i+1)).capitalize())
    return  '-'.join(res)

