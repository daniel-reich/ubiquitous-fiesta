
def find_fulcrum(lst):
    for i in range(len(lst)):
        sum_left = 0
        sum_right = 0
        for j in range(0, i):
            sum_left += lst[j]
        for j in range(i+1, len(lst)):
            sum_right += lst[j]
        if sum_left == sum_right:
            return lst[i]
​
    return -1

