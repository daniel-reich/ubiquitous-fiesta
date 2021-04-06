
def simplify_sqrt(n):
    lst=[]
    lst1=[]
    for i in range(2,n+1):
        if n%i*i==0:
            lst.append(i)
    print(lst)
    for j in lst:
        if pow(j,0.5)==int(pow(j,0.5)):
            lst1.append(j)
            lst1.sort()
    lst1=lst1[::-1]
    if len(lst1)==0:
        return 1,n
    else:
        return int((lst1[0])**0.5),int(n/(lst1[0]))

