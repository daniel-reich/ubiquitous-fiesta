
def shuffle_count(num):
    #gather data
    lst = list(range(1,num+1))
    lst2 = lst.copy()
    temp = []
    count = 0
    while temp != lst:
        temp = []
        for i in range(0,(num//2)):
            temp = temp + [lst2[i],lst2[i+(num//2)]]
        count += 1
        lst2 = temp
    return count

