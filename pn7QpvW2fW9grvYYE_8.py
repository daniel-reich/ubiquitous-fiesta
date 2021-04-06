
def find_fulcrum(lst):
    for i in range(len(lst)):
        if sum(lst[:i]) == sum(lst[i + 1:]):
            return lst[i]
    return -1

