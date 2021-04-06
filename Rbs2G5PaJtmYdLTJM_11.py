
def is_heteromecic(n):
    i = 0
    while i <= n:
        if i * (i + 1) == n:
            return True
        i += 1
    return False

