
def only_5_and_3(n):
    if n % 3 == 0:
        m = n//3
        m2 = n - 5
    else:
        m = n - 5
        m2 = None
    if m == 5 or m == 3 or m2 == 5 or m2 == 3:
        return True
    elif m > 1:
        if m2 is not None:
            return only_5_and_3(m) or only_5_and_3(m2)
        else:
            return only_5_and_3(m)
    else:
        return False

