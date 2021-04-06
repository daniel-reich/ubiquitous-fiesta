
def bonacci(sum_num, index):
    list = []
    for i in range(1, sum_num):
        list.append(0)
    list.append(1)
    
    for i in range(sum_num , index ):
        num = 0
        for j in range(1, sum_num + 1):
            num += list[i - j]
        list.append(num)
    return list[index - 1]

