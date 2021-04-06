
def sum_10(isbn):
    return sum(a*10 if b == 'X' else a*int(b) for a, b in enumerate(isbn[::-1], 1))
​
def sum_13(isbn):
    return sum(int(a)*int(b) for a, b in zip(isbn, '1313131313131'))
​
def isbn13(txt):
    if len(txt) == 13:
        return 'Valid' if sum_13(txt)%10 == 0 else 'Invalid'
    if sum_10(txt)%11 == 0:
        check = sum_13('978' + txt[:-1])%10
        return '978' + txt[:-1] + str(10 - check)
    return 'Invalid'

