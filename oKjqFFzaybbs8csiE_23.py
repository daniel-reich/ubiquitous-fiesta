
def cons(lst):
    ideal = list(range(min(lst), max(lst) + 1))
    lst.sort()
    if lst == ideal:
        return True
    return False

