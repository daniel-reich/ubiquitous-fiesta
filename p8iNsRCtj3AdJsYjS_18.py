
def title_to_number(s):
    return sum([f(i, x) for i, x in enumerate( s[::-1])])
​
def f(i, x):
    n = 1 + ord(x)- ord('A')
    return n * (26 ** i)

