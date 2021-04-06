
def longest_run(lst):
    long_list = []
    for i in range(len(lst)):
        j = i + 1
        yes = True
        a = [lst[j-1]]
        while (j < len(lst)) & (yes == True):
            if lst[j] == lst[j-1] +1:
                a.append(lst[j])
                yes = True
            elif lst[j] == lst[j-1] -1:
                a.append(lst[j])
                yes = True
            else:
                yes = False
            j += 1
        long_list.append(a)
    b = []
    for i in range(len(long_list)):
        if max(long_list[i]) - min(long_list[i]) + 1 == len(long_list[i]):
            b.append(long_list[i])
    c = []
    for i in range(len(b)):
        c.append(len(b[i]))
​
    return max(c)

