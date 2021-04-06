
def num_to_google(lst):
    d={'1':'g', '2':'o', '3':'l', '4':'e','6':'.'}
    res,x='',[]
    for word in lst:
        if type(word)==int:
            word=str(word)
        for i in word:
            if i in d:
                res+=d[i]
            if i=='5':
                res=res.title()
            if i=='7':
                res=res[0].swapcase()+res[1::]
            if i=='8':
                res=res[::-1]
        if '9' in word:
            res=''                
        x.append(res)
        res=''
    if 3545 in lst or 45 in lst:
        return ''.join(x).upper()
    return ''.join(x)

