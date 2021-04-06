
def how_many_missing(lst):
    if lst: return len(range(lst[0], lst[-1] + 1)) - len(lst)
    else: return 0

