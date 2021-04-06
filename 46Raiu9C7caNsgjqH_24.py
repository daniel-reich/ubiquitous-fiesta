
def compare_data(*args):
    return len([type(arg).__name__ for arg in args if isinstance(arg, type(list(args)[0]))]) == len(args)

