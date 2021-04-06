
from collections import Counter
def mode(nums):
    z=[]
    m=[]
    count=0
    d=Counter(nums)
    for key,values in d.items():
        z.append(values)
      
    for i,t in d.items():
        if t==max(z):
            count=count+1
            m.append(i)
       
   
    if count!=1:
        return sorted(m)
    else:
        return m

