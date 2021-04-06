
def is_heteromecic(n, i=0):
    if i * (i+1) < n:
        return is_heteromecic(n, i+1)
    return i * (i+1) == n

