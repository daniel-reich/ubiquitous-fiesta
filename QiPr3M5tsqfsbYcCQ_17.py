
def square_digits(n):
    lst = [int(d) for d in str(n)]
    return int(''.join(str(i**2) for i in lst))

