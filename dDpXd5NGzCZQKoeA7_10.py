
def num_args(func):
    args = []
    while True:
        try:
            func(*args)
        except TypeError:
            args.append(1)
        else:
            break
    return len(args)

