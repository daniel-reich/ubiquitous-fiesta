
def f(a, h):
    y=0
    while y**4-y*y*h*h+4*a*a>0 and y<h:
        y+=1/100     
    while y**4-y*y*h*h+4*a*a<0 and y<h:
        y-=1/100000
    if y<=0 or y>=h: return "Does not exist"
    x=2*a/y
    return sorted([round(x,3),round(y,3)])

