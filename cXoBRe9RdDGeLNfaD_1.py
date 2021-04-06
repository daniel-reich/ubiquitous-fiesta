
def eight_bit(exp):
    sep = ' + ' if ' + 'in exp else ' - '
    n1, n2 = [eval(x) for x in exp.split(sep)]
    ans = eval(exp)
    if any(-128 > x or x > 127 for x in [n1, n2, ans]):
        return 'Overflow'
    return ans, '{}{}{} = {}'.format(to_binr(n1), sep, to_binr(n2), to_binr(ans))
​
def to_bin(n):
    ans = []
    while n > 0:
        ans.append(n % 2)
        n //= 2
    return ''.join(str(b) for b in ans[::-1]) if ans else '0'
​
def to_binr(n):
    return to_bin(n) if n >= 0 else to_bin(256+n)

