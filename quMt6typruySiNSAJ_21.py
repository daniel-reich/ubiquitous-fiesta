
def shuffle(lst0):
    lst1 = []
    for i in range(len(lst0) // 2):
        lst1.append(lst0[i])
        lst1.append(lst0[(len(lst0)//2)+i])
    return lst1
​
​
def shuffle_count(num):
    lst0 = [i for i in range(num)]
    lst1 = shuffle(lst0)
    cnt = 1
    while True:
        if lst0 != lst1:
            lst1 = shuffle(lst1)
            cnt += 1
        else:
            return cnt

