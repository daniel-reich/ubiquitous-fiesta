
def twins(lst):
    return [idx for idx, num in enumerate(lst) if sum(lst[:idx]) == sum(lst[idx:])][0]

