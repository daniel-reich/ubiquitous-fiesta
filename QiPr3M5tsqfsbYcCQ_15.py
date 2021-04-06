
def square_digits(n):
    str_digit=str(n)
    digits=""
    for digit in str_digit:
        digits+=str(int(digit)**2)
    return int(digits)

