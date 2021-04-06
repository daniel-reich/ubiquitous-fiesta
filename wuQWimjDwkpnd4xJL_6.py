
def balanced(lst):
    if sum(lst[:int(len(lst)/2)]) == sum(lst[int(len(lst)/2):]):
        return lst
    elif sum(lst[:int(len(lst)/2)]) > sum(lst[int(len(lst)/2):]):
        return lst[:int(len(lst)/2)] * 2
    else: return lst[int(len(lst)/2):] * 2

