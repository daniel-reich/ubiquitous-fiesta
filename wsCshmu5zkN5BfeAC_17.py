
def divisible_by_left(n):
    s = str(n)
    return [f(s,i, x) for i, x in enumerate(s)]
​
def f(s, i, x):
    if i == 0:
        return False
    if s[i-1] == '0':
        return False
    return int(x) % int(s[i-1]) == 0

