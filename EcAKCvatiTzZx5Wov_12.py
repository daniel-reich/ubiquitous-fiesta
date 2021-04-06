
def resistor_code(c):
    b=['black','brown','red','orange','yellow','green','blue','violet','gray',\
       'white','gold','silver']
    v=[('0',0,'',''),('1',1,'+/-1%','100ppm/k'),('2',2,'+/-2%','50ppm/k'),\
       ('3',3,'','15ppm/k'),('4',4,'','25ppm/k'),('5',5,'+/-0.5%',''),\
       ('6',6,'+/-0.25%','10ppm/k'),('7',7,'+/-0.1%','5ppm/k'),\
       ('8',8,'+/-0.05%',''),('9',9,'',''),('',-1,'+/-5%',''),('',-2,'+/-10%','')]
    n=len(c)
    r=v[b.index(c[0])][0].lstrip('0')+v[b.index(c[1])][0]
    res=str(int(r)*10**v[b.index(c[2])][1])
    if n>4:
        r+=v[b.index(c[2])][0]
        t=v[b.index(c[4])][2]
        res=str(int(r)*10**v[b.index(c[3])][1])
    else:
        t=v[b.index(c[3])][2]
    rl=len(res)
    if rl<4 or res.find('.')>-1:
        res+='Ohm'
    elif 6>=rl>3:
        res=str(int(res)/10**3)+'kOhm'       
    elif 9>=rl>6:
        res=str(int(int(res)/10**6))+'MOhm'
    else:
        res=str(int(int(res)/10**9))+'GOhm'
    p=res.find('.0')
    if p>-1:
        res=res[:p]+res[p+2:]
    ans=res+' '+t
    if n==6:
        ans+=' '+v[b.index(c[5])][3]
    return ans

