
def priority_sort(lst, s):
    nlst = lst.copy()
    lst = [x for x in lst if x in s]
    nlst = [x for x in nlst if x not in s]
    return sorted(lst) + sorted(nlst)

