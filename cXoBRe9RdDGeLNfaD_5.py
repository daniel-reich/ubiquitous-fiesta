
import re
def eight_bit(exp):
    res = eval(exp)
    a, operator, b = re.findall(r"(-?\d*) ([+-]) (\d*)", exp)[0]
    a, b = int(a), int(b)
    if -128 > res or res > 127 or -128 > a or a > 127 or -128 > b or b > 127:
        return 'Overflow'
​
    def convert(n):
        return (bin(n)[2:] if n >= 0 else '1'
                + ''.join('0' if c == '1' else '1' for c in '{:0>7}'
                          .format(bin(~n)[2:])))
​
    return res, '{} {} {} = {}'.format(convert(a), operator, convert(b),
                                       convert(res))

