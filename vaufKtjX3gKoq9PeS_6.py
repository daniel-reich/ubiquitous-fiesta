
def ohms_law(v, r, i):
    if len([i for i in [v,r,i] if i==None])>=2:return 'Invalid'
    if len([i for i in [v,r,i] if i!=None])>=3:return 'Invalid'
    if v==None:return min([i for i in [v,r,i] if  i!=None])*max([i for i in [v,r,i] if i!=None])
    if r==None:return round(max([i for i in [v,r,i] if i!=None])/min([i for i in [v,r,i] if i!=None]))
    if i==None:return round(min([i for i in [v,r,i] if i!=None])/max([i for i in [v,r,i] if i!=None]),2)

