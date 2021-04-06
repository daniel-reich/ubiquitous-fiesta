
def is_repeated(strn):
    for i in range(1, 13):
        if 24 % i == 0:
            if strn[:i]*(24//i) == strn:
                return 24//i
    return False

