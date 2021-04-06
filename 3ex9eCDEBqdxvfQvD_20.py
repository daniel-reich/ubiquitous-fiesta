
def are_true(a, b):
    if a:
        if b:
            return "both"
        else:
            return "first"
    elif b:
        return "second"
    else:
        return "neither"

