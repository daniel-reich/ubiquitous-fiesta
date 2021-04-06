
def almost_sorted(lst):
    if is_seq(lst):
        return False
    else:
        if is_seq(lst[1:]) or is_seq(lst[:-1]):
            return True
        else:
            return any(is_seq(lst[:i]+lst[i+1:]) for i in range(1, len(lst)-1))
      
def is_seq(lst):
    return lst == sorted(lst) or lst[::-1] == sorted(lst)

