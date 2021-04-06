
def digit_sort(lst):
    lst.sort()
    return sorted(lst, key=lambda x: len(str(x)), reverse=True)

