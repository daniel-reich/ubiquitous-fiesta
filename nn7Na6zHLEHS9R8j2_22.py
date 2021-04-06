
def deep_count(lst):
    if len(lst)==0:
        return 0
    else:
        if isinstance(lst[0],list):
            return 1+deep_count(lst[0])+deep_count(lst[1:])
        else:
            return 1+deep_count(lst[1:])

