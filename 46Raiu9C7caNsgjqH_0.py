
def compare_data(*args):
    return len(set(type(i) for i in args)) == 1 if args else True

