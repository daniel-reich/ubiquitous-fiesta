
def digits(number):
    n, count_zeros = number - 1, 0
    len_str_n = len(str(n))
    for i in range(1, len_str_n):
        count_zeros += 9 * 10 ** (i - 1) * (len_str_n - i)
    return n * len_str_n - count_zeros

