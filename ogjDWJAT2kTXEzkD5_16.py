
def all_truthy(*args):
    return all(bool(x) for x in args)

