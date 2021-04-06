
def square_digits(n):
    curdigit = 0
    final = ""
    while n > 0:
        curdigit = n % 10
        n = n // 10
        final = str(curdigit ** 2) + final
​
    final = int(final)
    print(final)
    return final

