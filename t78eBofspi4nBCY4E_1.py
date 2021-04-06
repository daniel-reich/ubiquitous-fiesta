
def base_conv(n, b):
    if type(n) is int:
        res = ''
        while n:
            res += chr(97 + n % b)
            n = n // b
        return res[::-1]
    else:
        res = 0
        for i in range(1, len(n) + 1):
            if 96 < ord(n[-i]) < 97 + b:
                res += (ord(n[-i]) - 97) * b ** (i - 1)
            else:
                return '{} is not a base {} number.'.format(n, b)
        return res

