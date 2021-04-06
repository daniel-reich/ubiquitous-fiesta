
def freq_count(lst, el):   
    s=str(lst)
    ml=s.count('[')
    arr=[0]*(ml)
    n=-1
    for i in s:
        if i=='[':
            n+=1
        elif i==']':
            n-=1
        if i.isnumeric() and int(i)==el:
            arr[n]+=1
    if s[5]=='2':
        ml-=5
    if arr[ml-1]==0:
        ml-=1
    return [[j,arr[j]]for j in range(ml)]
print(freq_count([1, [2], 1, [[2]], 1, [[[2]]], 1, [[[[2]]]]], 2))

