
def shuffle_count(num):
    count=1
    lst=[i for i in range(1,num+1)]
    n=num//2
    lst1=lst[:n]
    lst2=lst[n:]
    b=shuffle(lst1,lst2)
    while True:
        if lst==b:
            break
        else:    
            count+=1
            lst1=b[:n]
            lst2=b[n:]
            b=shuffle(lst1,lst2)
    return count              
def shuffle(list1, list2):
    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1
    else:
        return [list1[0],list2[0]] + shuffle(list1[1:], list2[1:])

