
def smith_type(number):
    if len(g_f(number)) == 1:
        return "Trivial Smith"
    elif g_r(number) != g_r(sum(g_f(number))):
        return "Not a Smith"
    if g_r(number - 1) == g_r(sum(g_f(number - 1))) and len(g_f(number - 1)) != 1:
        return "Oldest Smith"
    elif g_r(number + 1) == g_r(sum(g_f(number + 1))) and len(g_f(number + 1)) != 1:
        return "Youngest Smith"
    return "Single Smith"
    
def g_r(x):
    if len(str(x)) == 1:
        return x 
    else: 
        x = sum([int(i) for i in str(x)])
        return g_r(x)
​
def g_f(x):
    factors = []
    i = 2
    while x != 1:
        if x % i == 0:
            factors.append(i)
            x = x // i
            i = 1
        i += 1
    return factors

