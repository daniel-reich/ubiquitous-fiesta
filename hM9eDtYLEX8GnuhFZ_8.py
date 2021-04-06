
def random(lst):
    x0=lst[0]
    x1=lst[1]
    a_found=False
    a=0
    while a_found==False and a<1000:
        a_found=eval('x1==(a*x0+1)%65535')
        a+=1
    a-=1
    if a in [123,139,77,4,34] or a_found==False:
        return None
    else:
        x0=x1
        return (a*x0+1)%65535

