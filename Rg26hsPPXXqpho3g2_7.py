
def which_is_larger(f, g):
    a = f()
    b = g()
    if a > b:
        return 'f'
    elif a < b:
        return 'g'
    else:
        return 'neither'

