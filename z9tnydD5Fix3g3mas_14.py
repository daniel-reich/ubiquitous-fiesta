
def check_pattern(lst,pat):
 dic=[(j,i) for i,j in zip(lst,pat)]
 if len([i for i in lst if lst.count(i)>1]) == len([i for i in pat if pat.count(i)>1]):
    if len([i for i in dic if dic.count(i)>1]) == len([i for i in pat if pat.count(i)>1]):
     return all([i for i in dic if dic.count(i)>1])
    else:
     return len([i for i in pat if pat.count(i)>1])==0
 else:
     return False

