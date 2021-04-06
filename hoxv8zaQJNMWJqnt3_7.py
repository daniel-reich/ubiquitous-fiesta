
def is_heteromecic(n,m=0):
    return m <= n**0.5 and (m * (m + 1) == n or is_heteromecic(n, m + 1))

