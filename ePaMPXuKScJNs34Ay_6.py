
def add_it_up(lst):
    t = type(lst[0])
    if t in [int, float]: return sum(lst)
    if t == list: return sum(lst, [])
    if t == tuple: return sum(lst, ())

