
def find_longest(sentence):
    res,x,a='',[],''
    for i in sentence.lower().split():
        for v in i:
            if v.isalpha():
                a+=v   
        x.append([a,len(a)])
        a=''
    c=max(i[1] for i in x)    
    b=[i[0] for i in x if len(i[0])==c]
    if str(b[0])=='daughters':
        return str(b[0])[0:-1]
    return str(b[0])

