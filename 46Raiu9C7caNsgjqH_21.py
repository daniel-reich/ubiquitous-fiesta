
def compare_data(*args):
    if not args:
        return True
    return len(set([type(x) for x in args])) == 1

