
def is_heteromecic(n, a=0):
    if a * (a + 1) > n:
        return False
    elif a * (a + 1) == n:
        return True
    else:
        return is_heteromecic(n, a + 1)

