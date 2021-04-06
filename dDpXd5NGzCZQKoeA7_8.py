
def num_args(func):
    pas, n = False, 0
    while not pas:
        try:
            eval('func' + str(tuple(range(n))))
            pas = True
        except TypeError:
            n += 1
    return n

