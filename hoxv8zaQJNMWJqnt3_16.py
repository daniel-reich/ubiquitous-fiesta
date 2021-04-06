
def is_heteromecic(n, k=0):
    if n == k * (k + 1):
        return True
    if n < k * (k + 1):
        return False
    return is_heteromecic(n, k + 1)

