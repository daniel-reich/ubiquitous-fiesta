
def is_shifted(lst1, lst2):
    res = []
    for i in range(len(lst1)):
        res.append(lst1[i] - lst2[i])
    return len(set(res))==1
  
​
def is_multiplied(lst1, lst2):
    if lst2[0]==0 and lst2[1]==0 and lst2[2]==0:return True
    if lst2[0]==0 and lst2[1]==0 and lst2[2]!=0:return False
    res = []
    for i in range(len(lst1)):
        res.append(lst1[i] / lst2[i])
    return len(set(res))==1

