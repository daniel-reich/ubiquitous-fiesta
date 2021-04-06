
def shift_sentence(txt):
    str=""
    drk=txt.split()
    d=[]
    p=[]
  
    for i in drk:
        d.append(i[0])
        p.append(i[1:])
    for a in range(len(d)):
        if a==0:
            str+=d[-1]+p[a]+""
       
       
        else:
            str=str+" "+d[a-1]+p[a]+""
         
             
    return str

