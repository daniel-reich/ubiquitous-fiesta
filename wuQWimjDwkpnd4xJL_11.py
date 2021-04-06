
def balanced(lst):
    if sum(lst[len(lst)//2:])==sum(lst[:len(lst)//2]):
        return lst
    elif sum(lst[len(lst)//2:])>sum(lst[:len(lst)//2]):
        return lst[len(lst)//2:] + lst[len(lst)//2:]
    else:
        return lst[:len(lst)//2] +lst[:len(lst)//2]

