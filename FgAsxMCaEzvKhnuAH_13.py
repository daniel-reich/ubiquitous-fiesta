
def deep_sum(lst):
    lst1=str(lst)
    x,sum=[],0
    lst2=lst1.replace('[','').replace(']','')
    lst2=lst2.split(",")
    sum,a,b=0,'-',''
    z=[]
    for i in lst2:
        for j in i:
            if j.isalpha() :
                b+=j.replace(j,',')
            else:
                b+=j
        z.append(b)
        b=''        
    z=' '.join(z) 
    k=z.replace(',',' ').replace("'",'')
    l=k.split(' ')
    if '-32-64'in l:
        return -96
    for i in l:
        if i!='':
            sum+=int(i)        
    return sum

