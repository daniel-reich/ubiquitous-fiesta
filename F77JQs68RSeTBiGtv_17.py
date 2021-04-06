
def diamond_sum(num):
    if num == 1:
        return 1
​
    mid1 = (num + 1)  // 2
    mid2 = ((num ** 2 - num + 1) + (num ** 2)) // 2
    res = mid1 + mid2
​
    for i in range(num - 2):
        s = num + (num * i) + 1
        e = s + num - 1
        res = res + (s + e)
​
    return res

