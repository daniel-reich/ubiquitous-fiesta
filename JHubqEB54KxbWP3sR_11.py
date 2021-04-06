
def dist(line, x, y):
    record=0
    record2=0
    m=''
    b=''
    for character in line:
        if record==1:
            m+=character
        if character=='=':
            record=1
        if character=='x':
            record=0
            m=m.replace('x','')
    m2=eval(m)
    for character in line:
        if record2==1:
            b+=character
        if character=='x':
            record2=1
    b2=eval(b)
    perpm=-1/m2
    perpb=y-perpm*x
    intx=(perpb-b2)/(m2-perpm)
    inty=(m2*intx+b2)
    return round((((x-intx)**2+(y-inty)**2)**.5)*100)/100

