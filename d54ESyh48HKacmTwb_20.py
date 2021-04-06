
def gcd(lst):
    result = 0
    new_lst = []
    for i in range(1, max(lst)):
        for j in lst:
            if j % i == 0:
                new_lst.append(i)
    repeat_lst = []
    for i in new_lst:
        if new_lst.count(i) == len(lst):
            repeat_lst.append(i)
    return max(repeat_lst)

