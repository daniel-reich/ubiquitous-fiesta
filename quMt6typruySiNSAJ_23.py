
def shuffle_count(number):
    alist = [x for x in range(1,number+1)]
    middle = len(alist) // 2
    left_half = alist[:middle]
    right_half = alist[middle:]
    count = 0
    shuffle_count_number = 0
    while count == 0 or newlist != alist:
        newlist = []
        for i in range(len(left_half)):
            newlist.append(left_half[i])
            newlist.append(right_half[i])
        count += 1
        left_half = newlist[:middle]
        right_half = newlist[middle:]
    print(newlist)
    print(count)
    return count

