
def simplify(txt):
    a, b = int(txt[:txt.index('/')]), int(txt[txt.index('/') + 1:]) # a: numerator, b: denominator
    if a % b == 0: return str(int(a / b)) # Can be divided
​
    divisible = [i for i in range(2, min(a + 1, b)) if a % i == 0 and b % i == 0]
    # Makes list of numbers that both a and b can be divided with
    
    if divisible == []: return txt # No divisibles, return original txt
​
    a, b = int(a / divisible[-1]), int(b / divisible[-1])
    return '{}/{}'.format(a, b) # Divide both a and b, put them together, return

