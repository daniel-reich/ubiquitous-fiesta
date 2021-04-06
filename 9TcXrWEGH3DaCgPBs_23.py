
def find_odd(lst):
    import collections as c
    x = list(c.Counter(lst).items())
​
    return [i[0] for i in x if i[1]%2 !=0][0]

