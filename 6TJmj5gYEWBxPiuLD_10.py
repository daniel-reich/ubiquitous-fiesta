
def seating_students(lst):
    k=0
    a=[i for i in range(1,lst[0]+1) if i not in lst[1:]]
    for i in range(len(a)-1):
        if (a[i+1]-a[i]==1 and a[i]%2==1) or (a[i+1]-a[i]==2):
            k+=1
        if i<len(a)-2 and a[i+2]-a[i]==2:
            k+=1
    return k

