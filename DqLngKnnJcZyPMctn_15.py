
def stock_picker(lst):
    mx = [y-x for i,x in enumerate(lst) for y in lst[i:] if y-x>0]
    return max(mx) if mx else -1

