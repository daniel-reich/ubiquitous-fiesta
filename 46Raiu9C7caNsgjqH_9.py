
def compare_data(*args):
    return not args or len(set(map(type, args))) == 1

