
def is_heteromecic(n):
    return True if n == 0 else any([1 for i in range(n) if i * (i + 1) == n])

