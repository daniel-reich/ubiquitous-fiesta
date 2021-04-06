
def convert10_to_base(n, base):
    result, extra_digits = '', 'ABCDEF'
    while n > 0:
        remainder = n % base
        if remainder < 10:
            result += str(remainder)
        else:
            result += extra_digits[remainder - 10]
        n = n // base
    return result[::-1]
​
​
def esthetic(num):
    res = []
    for base in range(2, 11):
        str_num = convert10_to_base(num, base)
        if all(abs(int(str_num[i]) - int(str_num[i - 1])) == 1
               for i in range(1, len(str_num))):
            res.append(base)
    return res if res else 'Anti-Esthetic'

