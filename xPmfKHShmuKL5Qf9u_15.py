
def scale_tip(lst):
    middle = lst.index('I')
    x = (sum(lst[:middle]))  # Left half
    z = (sum(lst[-middle:]))  # Right half
    if x == z:
        return 'balanced'
    elif x > z:
        return 'left'
    elif x < z:
        return 'right'

