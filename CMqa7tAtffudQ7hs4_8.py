
def sorting_steps(lst):
    arr=lst[:]
    s=[]
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            if arr[j]<arr[i]:
                s.append((i,j))
                arr[j],arr[i]=arr[i],arr[j]      
    return s

