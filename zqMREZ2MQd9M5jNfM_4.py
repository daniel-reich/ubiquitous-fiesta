
def is_symmetrical(num):
    x = list(str(num))
    y = list(reversed(str(num)))
    if x != y:
        return False
    else:
        return True

