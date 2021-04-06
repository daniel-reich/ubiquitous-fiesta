
def priority_sort(lst, s):
    return sum([[i]*lst.count(i) for i in s if i in lst] + sorted([[i] for i in lst if i not in s]), [])

