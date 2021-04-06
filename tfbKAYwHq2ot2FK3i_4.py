
def variation_n_k(n, k) -> int:
    res = 1
    for i in range(n, n - k, -1):
        res *= i
    return res
​
​
def non_repeats(base):
    sum = 0
    for i in range(2, base + 1):
        sum += variation_n_k(base, i)
    return sum//base * (base - 1) + base - 1

