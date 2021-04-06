
def which_is_larger(f, g):
    f,g = f(),g()
    return 'neither' if f==g else 'f' if f>g else 'g'

