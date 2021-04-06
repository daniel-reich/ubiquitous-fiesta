
def ohms_law(v, r, i):
    x =[v,r,i].count(None)
    if x==2 or x==0:return 'Invalid'
    ans = r*i if not v else v/i if not r else v/r
    return round(ans,2)

