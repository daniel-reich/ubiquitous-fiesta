
def which_is_larger(f, g):
    return {
        f() >  g(): 'f',
        f() <  g(): 'g',
        f() == g(): 'neither',
    }[True]

