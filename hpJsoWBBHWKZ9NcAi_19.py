
def bird_code(lst):
    res=[]
    for x in lst:
        x=x.replace('-',' ')
        if len(x.split())==1:
            res.append(x[:4].upper())
        elif len(x.split())==2:
            res.append(x.split()[0][:2].upper()+x.split()[1][:2].upper())
        elif len(x.split())==3:
            res.append(x.split()[0][0].upper()+x.split()[1][0].upper()+x.split()[2][:2].upper())
        elif len(x.split())==4:
            res.append(''.join([s[0].upper() for s in x.split()]))
    return res

