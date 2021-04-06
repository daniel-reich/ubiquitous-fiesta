
def is_heteromecic(n):
    k = int(round(-.5 + pow(n + .25, .5), 0))
    return n == k * (k + 1)

