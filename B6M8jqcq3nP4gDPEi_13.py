
def iso_group(lst):
    max_item = __iso_group(lst)
    if lst.count(max_item) >= 2:
        return [max_item, max_item]
    return max_item
​
def __iso_group(lst):
    if len(lst) == 1:
        return lst[0]
    return max(lst[0], __iso_group(lst[1:]))

