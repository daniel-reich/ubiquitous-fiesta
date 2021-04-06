
def num_args(func):
    n_args = 0
    trying = True
    while trying:
        new_args = [1] * n_args
        try:
            ans = func(*new_args)
            trying = False
        except TypeError:
            n_args += 1
    return n_args

