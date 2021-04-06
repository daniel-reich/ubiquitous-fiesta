
def is_valid_subsequence(lst, sequence):
    while len(sequence) > 0:
        k = sequence.pop(0)
        if k not in lst:
            return False
        lst = lst[lst.index(k)+1:]
    return True

