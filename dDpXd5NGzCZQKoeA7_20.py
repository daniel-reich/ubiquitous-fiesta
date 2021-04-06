
def num_args(func):
    arg = []
    while True:
        try:
            eval('func(*arg)')
            break
        except TypeError:
            arg.append(1)
    return len(arg)

