
def numbers_to_ranges(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return ['{}'.format(lst[0])]
    begin = lst[0]
    res = []
    for i in range(1, len(lst)):
        if lst[i] != lst[i - 1] + 1 or i == len(lst) - 1:
            end = lst[i - 1] if i < len(lst) - 1 else lst[i]
            if end > begin:
                res.append('{}-{}'.format(begin, end))
            else:
                res.append('{}'.format(begin))
            begin = lst[i]
    return res

