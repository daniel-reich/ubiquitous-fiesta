
def fifth(*args):
    l=len(args)
    return type(args[4]) if l>=5 else "Not enough arguments"

