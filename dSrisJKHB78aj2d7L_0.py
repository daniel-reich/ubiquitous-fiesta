
def triangle(p,a):
    r=[]
    s=p/2
    for x in range(1,p//2+1):
        for y in range(int(s-x+1),p//2+1):
                z=p-x-y
                if round((s*(s-x)*(s-y)*(s-z))**.5,5)==a:
                    new=sorted((x,y,z))
                    if new not in r:
                        r.append(new)
    return sorted(r)

