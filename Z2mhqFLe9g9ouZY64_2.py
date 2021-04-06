
def is_valid_subsequence(lst, sequence):
    for i in range(len(lst)):
        if lst[i]==sequence[0]:sequence.pop(0)
        if len(sequence)==0:return True
    return  False

