
def alternate_sort(lst):
    lst.sort(key=lambda v: (isinstance(v, str), v))
    return [lst[i+j] for i in range(len(lst)//2) for j in [0, len(lst)//2]]

