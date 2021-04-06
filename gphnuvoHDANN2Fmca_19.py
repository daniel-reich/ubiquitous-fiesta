
def odd_sort(lst):
    lstcopy = lst[:]
    oddlist = []
    for i in lst:
        if i%2!=0:
            oddlist.append(i)
    oddlist.sort()
    
    i = 0
    for j in range(len(lstcopy)):
        if lstcopy[j]%2!=0:
            lstcopy[j]=oddlist[i]
            i+=1
    return lstcopy

