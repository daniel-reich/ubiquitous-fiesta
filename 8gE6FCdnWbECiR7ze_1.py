
def prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
​
​
​
​
def digital_root(x):
    s = 0
    for i in str(x):
        s += int(i)
    if s > 9:
        return digital_root(s)
    else:
        return s
​
​
​
​
def prime_factors(x):
    s = []
    for i in [2] + list(range(3, x)):
        while x%i == 0:
            x /= i
            s.append(i)
    return s
​
​
inRecursion = False
​
def smith_type(number):
    global inRecursion
    if prime(number):
        return "Trivial Smith"
    x = digital_root(number)
    y = digital_root(sum(prime_factors(number)))
    
    if x != y:
        return "Not a Smith"
    if not inRecursion:
        inRecursion = True
        if smith_type(number+1) == "Smith":
            inRecursion = False  
            return "Youngest Smith"
        elif smith_type(number-1) == "Smith":
            inRecursion = False  
            return "Oldest Smith"
        else:
            inRecursion = False
            return "Single Smith"   
    return "Smith"

