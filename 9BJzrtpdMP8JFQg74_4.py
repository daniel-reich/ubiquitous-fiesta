
def twins(lst):
    s_half, s_acc = sum(lst) / 2, 0
    for i in range(len(lst)):
        s_acc += lst[i]
        if s_acc == s_half:
            return i + 1
    return 'not found'

