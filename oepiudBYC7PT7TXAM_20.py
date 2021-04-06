
def parse_roman_numeral(num):
    o={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    u=[]
    for i in range(len(num)):
        u.append(o[num[i]])
    u.append(0)
    final=[]
    for i in range(len(u)-1):
        if u[i]>=u[i+1] or u[i]==0:
           final.append(u[i])
        else:
            final.append(u[i+1]-u[i])
            u[i+1]=0
    return sum(final)

