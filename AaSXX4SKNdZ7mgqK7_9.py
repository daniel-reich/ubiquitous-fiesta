
def first_one(*a):
    return next((i for i in a if bool(i)), False) or "not found"

