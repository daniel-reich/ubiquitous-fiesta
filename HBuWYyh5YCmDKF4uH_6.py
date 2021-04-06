
def almost_sorted(lst):
    if sum([lst[i] < lst[i+1] for i in range(len(lst)-1)])==len(lst)-2 or sum([lst[i] < lst[i+1] for i in range(len(lst)-1)])==1:
        return True
    return False

