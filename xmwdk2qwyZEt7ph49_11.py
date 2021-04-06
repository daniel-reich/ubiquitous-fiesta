
def get_length(lst):
    return sum( 1 if not isinstance(x, list) else get_length(x) for x in lst)

