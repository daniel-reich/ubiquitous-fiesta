
def which_is_larger(f, g):
    return ['f','g', 'neither'][(g()>f())-(g()==f())]

