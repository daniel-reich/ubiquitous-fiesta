
def longest_substring(digits):
    digits=digits+digits[-1]
    lst=list(map(int,digits))
    lst1=list(lst)
    for i in range(len(lst)):
        if lst[i]%2==0:
            lst[i]='E'
        else:
            lst[i]='O'
    j=0
    substrings=[]
    while True:
        if j==len(lst):
            break
        last=lst[j]
        for k in range(j,len(lst)):
            if lst[k]!=last:
                last=lst[k]
            else:
                substrings.append(''.join(str(e) for e in lst1[j-1:k]))
                j=k+1
                continue
    maxstr=1
    sub=None
    for i in substrings:
        if len(i)>maxstr:
            maxstr=len(i)
            sub=i
    return sub

