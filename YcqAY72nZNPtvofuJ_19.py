
def quad_sequence(lst):
    c=lst[0]
    a=(lst[2]-2*lst[1]+c)//2
    b=lst[1]-a-c
    s=[]
    for i in range(len(lst)):
        j=i+len(lst)
        s.append(a*j**2+b*j+c)
    return s

