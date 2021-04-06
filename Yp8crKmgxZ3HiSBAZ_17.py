
def helper_freq_count(lst, el, recursive_level, freq_lst):
    """
    go through every element and recursively call this func
    """
    if len(freq_lst) < recursive_level + 1:
        freq_lst.append([recursive_level, 0])
​
    instances = 0
    for i in lst:
        if i == el: #every element found
            instances += 1
        if isinstance(i, list): #if it's a list, recurse
            freq_lst = helper_freq_count(i, el, recursive_level+1, freq_lst)
​
    freq_lst[recursive_level][1] += instances
​
    return freq_lst
​
def freq_count(lst, el):
    return helper_freq_count(lst, el, 0, [])

