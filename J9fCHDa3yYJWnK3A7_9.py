
def is_happy(n, found=set()):
    if n == 1:
        return True
    if n in found:
        return False
    new = sum(int(i)**2 for i in str(n))
    return is_happy(new, found | {n})

