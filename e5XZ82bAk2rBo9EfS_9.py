
def bed_time(*times):
    a=[]
    for t in range(len(times)):
        h=int(times[t][0][:2])-int(times[t][1][:2])
        h=h+24*(h<0)
        m=int(times[t][0][3:])-int(times[t][1][3:])
        if m<0:
            h-=1
            m+=60
        a.append('0'*(h<10)+str(h)+':'+'0'*(m<10)+str(m))
    return a

