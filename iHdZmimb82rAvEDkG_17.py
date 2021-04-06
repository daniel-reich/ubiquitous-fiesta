
def bitwise_index(lst):
    a=['odd','even']
    m=-999;msg=''
    for i in range(len(lst)):
        d=lst[i]//2
        if d==lst[i]/2 and d>m:
            m=d
            msg=a[i//2==i/2]
            f=i
    if msg:
        return {'@'+msg+' index '+str(f):lst[f]}
    return 'No even integer found!'

