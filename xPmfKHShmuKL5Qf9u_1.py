
def scale_tip(lst):
    m = len(lst)//2
    L, R = sum(lst[:m]), sum(lst[-m:])
    return 'left' if L > R else 'right' if R > L else 'balanced'

