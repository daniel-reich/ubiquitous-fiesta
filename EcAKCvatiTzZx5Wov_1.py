
def resistor_code(colors):
    d1={'black':0,'brown':1,'red':2,'orange':3,'yellow':4,'green':5,
        'blue':6,'violet':7,'gray':8,'white':9,'gold':-1,"silver":-2}
    mg={'black':0,'brown':'+/-1%','red':'+/-2%','green':'+/-0.5%',
        'blue':'+/-0.25%','violet':'+/-0.1%','gray':'+/-0.05%','gold':'+/-5%','silver':'+/-10%'}
    tcr={'brown':'100ppm/k','red':'50ppm/k','orange':'15ppm/k','yellow':'25ppm/k',
         'blue':'10ppm/k','violet':'5ppm/k'}
    res=''
    if len(colors)==4:
        x=colors[0:2]
        for i in x:
            if i in d1:
                res+=str(d1[i])      
        if colors[2] in d1:
            a=colors[2]
            b=10**(d1[a])
            if 10**(d1[a])==10**6:
                res=str(int((int(res)*b)/10**6))+'MOhm'
            if b==10**2 or b==10**3:
                res=str((int(res)*(b))/1000)+'kOhm'
            if b==10**(0) or b==10**(-2) :
                res=str((int(res)*(b)))+'Ohm'
        if colors[-1] in mg:
            res+=' '+mg[colors[-1]]
        return res.strip()   
    if len(colors)==5:
        for i in colors[0:3]:
            if i in d1:
                res+=str(d1[i])
        if colors[3] in d1:
            a=colors[3]
            b=10**(d1[a])
            if b==10**6:
                res=str(int((int(res)*(b))/10**6))+'MOhm'
            if b==1000:
                res=str((int(res)*(b))/1000)+'kOhm'
            if b==10**(-1)or b==10**(-2):
                res=str((int(res)*b))+'Ohm'
        if colors[4] in mg:
            res+=' '+mg[colors[-1]]
        return res.strip()        
    else:
        for i in colors[0:3]:
            if i in d1:
                res+=str(d1[i])
        if colors[3] in d1:
            a=colors[3]
            b=10**(d1[a])
            if b==1000000000:
                res=str(int((int(res)*(b))/10**9))+'GOhm'
            if b==10**6:
                res+='Mohm'
            if b==1000:
                res=str(int((int(res)*b)/1000))+'kOhm'
            if b==10**0:
                res=str(int(res)*b)+'Ohm'
        if colors[4] in mg:
            res+=' '+mg[colors[4]]
        if colors[5] in tcr:
            res+=' '+tcr[colors[5]]
        return res

