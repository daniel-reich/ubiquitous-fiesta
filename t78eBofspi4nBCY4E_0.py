
def base_conv(n, b):
    if type(n) == int:
        res = ''
        while n > 0:
            n, i = divmod(n, b)
            res += str(chr(i + 97))
        return res[::-1]
​
    res = 0
    for idx, i in enumerate(n[::-1]):
        val = ord(i) - 97
        if val >= b or not i.isalpha():
            return '{} is not a base {} number.'.format(n, b)
        res += (ord(i) - 97)*b**idx
    return res

