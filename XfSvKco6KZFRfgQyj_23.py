
def find_a_seat(n, lst):
    o=  [round((i/(n/len(lst)))*100,2) for i in lst]
    f=[]
    for i in o:
        if i<50:
            f.append(i)
    if len(f)==0:return -1
    if round(sum(f))==50:return 0
    y= [o.index(i) if i<50 else i for i in o]
    return [x for x in y if x<10][0]

