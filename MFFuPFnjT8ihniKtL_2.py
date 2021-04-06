
def bug_jump(height, time):
    dir=['down',None,'up']
    f=height**.5-time/1000
    h=height-f**2
    hh=round(abs(h*(h>0)),2)
    return[hh,dir[2*(f>0)+(h<0)]]

