
def base_conv(n, b):
    def dec_to_base(n, b):
        if n == 0: return 'a'
        s = ''
        while n:
            n, r = divmod(n, b)
            s = chr(97+r) + s
        return s
​
    def base_to_dec(s, b):
        if max(s) > chr(96 + b) or not all(c.isalpha() for c in s):
            return '{} is not a base {} number.'.format(s, b)
        n = 0
        for c in s:
            n = n * b + ord(c) - 97
        return n
​
    return dec_to_base(n, b) if isinstance(n, int) else base_to_dec(n, b)

