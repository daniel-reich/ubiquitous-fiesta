
def no_perms_digits(n):
​
    factorial = 1
​
    for num in range(1, n + 1):
        factorial *= num
​
    return len(str(factorial))

