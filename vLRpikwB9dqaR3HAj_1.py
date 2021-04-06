
def is_ord_sub(small, big):
    try:
        for i in small:
            big = big[big.index(i)+1:]
    except ValueError:
        return False
    return True

