
def multiplicity(lst):
    return [
        [num, lst.count(num)]
        for index, num in enumerate(lst)
        if index == lst.index(num)
    ]

