
def is_slidey(n):
    n = list(str(n))
    if(len(n)==1):return True
    for i in range(len(n)-1):
        if abs(int(n[i+1])- int(n[i]))!=1:return False
    return True

