
def is_heteromecic(n):
    i, k = 0, 0
    while i <= n:
        if n == i:
            return True
        k += 2
        i += k
    return False

