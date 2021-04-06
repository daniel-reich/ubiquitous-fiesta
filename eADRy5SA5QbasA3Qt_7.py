
def is_harshad(n):
    sum_n = 0
    for i in str(n):
        sum_n += int(i)
    return True if n % sum_n == 0 else False

