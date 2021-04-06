
def cycle_length(lst, n):
    count = 0
    ct_index = n
​
    return work(lst, ct_index, count)
​
​
def work(lst, ct_index, count):
    if ct_index <= len(lst):
        if ct_index == lst[ct_index - 1]:
            return count
​
        lst[lst[ct_index - 1] - 1], lst[ct_index - 1] = lst[ct_index - 1], lst[lst[ct_index - 1] - 1]
        ct_index = lst[ct_index - 1]
        count += 1
​
        return work(lst, ct_index, count)
​
    else:
        srtd = sorted(lst)
        srtd_id = find_id(srtd, ct_index)
​
        if ct_index == lst[srtd_id]:
            return count
​
        x = lst[srtd_id]
        t_id = find_id(lst, ct_index)
        lst[srtd_id] = lst[find_id(lst, ct_index)]
        lst[t_id] = x
        count += 1
        ct_index = x
        return work(lst, ct_index, count)
​
​
def find_id(lst, num):
    for i in range(len(lst)):
        if lst[i] == num:
            return i
    return -1

