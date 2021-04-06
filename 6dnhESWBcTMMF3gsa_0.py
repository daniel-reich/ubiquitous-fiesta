
def stupid_addition(a, b):
    if type(a) == type(b):
        if type(a) == int:
            return str(a) + str(b)
        return int(a)+int(b)

