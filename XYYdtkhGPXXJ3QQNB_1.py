
def num_in_str(lst):
    arr = []
    for s in lst:
        if any(i.isdigit() for i in s):
            arr.append(s)
    return arr

