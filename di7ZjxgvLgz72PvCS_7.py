
def A(a,b):
    count=0
    if len(a)!=len(b):
        return False
    for i in range(len(a)):
        if a[i]!=b[i]:
            count+=1
    return count==2
        
    
def validate_swaps(lst, txt):
    T=[]
    for i in lst:
        if A(i,txt):
            T.append(True)
        else :
            T.append(False)
    return T

