
def final_result(lst):
    s=[]
    i=0
    j=0
    a=0
    while i<len(lst):
        if len(s)==0:
            a=lst[i]
            s.append(lst[i])
            j=1
            i+=1
        elif a==lst[i]:
            j=2
            i+=1
        elif a!=lst[i] and j==2:
            s.pop()
            if len(s)==0:
                s.append(lst[i])
                j=1
                a=lst[i]
                i+=1
            else :
                a=s[-1]
                j=1
        elif a!=lst[i] and j==1 :
            a=lst[i]
            s.append(lst[i])
            i+=1
        if i==len(lst) and j==2:
            s.pop()
    return s

