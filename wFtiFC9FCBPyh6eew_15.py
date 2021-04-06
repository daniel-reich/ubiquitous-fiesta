
def split_into_lists(n):
    if n == 0:
        return [[0]]
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[2], [1, 1]]
    elif n == 3:
        return [[3], [2, 1], [1, 1, 1]]
    else:
        res = [[n]]
        for k in range(n - 1, 0, -1):
            for lst in split_into_lists(n - k):
                tmp_lst = sorted([k] + lst, reverse=True)
                if tmp_lst not in res:
                    res.append(tmp_lst)
        return res
​
​
def partitions(n):
    return len(split_into_lists(n))

