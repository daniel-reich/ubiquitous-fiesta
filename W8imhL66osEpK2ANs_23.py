
def time(dct, people, walls):
    A = dct.get('walls')
    x = dct.get('people')
    t = dct.get('minutes')
    n = A / (x * t)
    print(n)
    import math
    time = math.ceil(walls / (people * n))
    return time

