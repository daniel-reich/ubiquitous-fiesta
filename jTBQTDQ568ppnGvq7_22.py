
def digit_sort(lst):
    z = sorted(lst)
    return sorted(z, key=lambda x:len(str(x)), reverse=True)

