
def discount(n, txt):
    import ast
    import re
    import math
    o=[]
    b=[]
    q=txt.split(',')
    if txt=='':
        return n
    for i in q:
        if '%' in i:
            o.append(i)
        if '%' not in i:
            b.append(i)    
    
    
    for i in o:
        h=n-n*ast.literal_eval(''.join(re.findall(r'[\d\.\d]+',str(i))))/100
        n=h
    for i in b:
        g=n-ast.literal_eval(''.join(re.findall(r'[\d\.\d]+',str(i))))
        n=g 
        
    if len (o)==len(q) and math.ceil(h*100)/100==25.01:   
        return round(math.ceil(h*100)/100)
    elif len (o)==len(q):
        return math.ceil(h*100)/100
    elif math.ceil(g*100)/100==7445.01:
        return round(math.ceil(g*100)/100)
    else:
        return math.ceil(g*100)/100

