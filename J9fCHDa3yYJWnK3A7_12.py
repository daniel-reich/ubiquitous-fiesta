
def is_happy(num):
    if num == 1:
        return True
    elif num == 4:
        return False
    return is_happy(sum(int(c) * int(c) for c in str(num)))

