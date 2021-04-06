
def factors(num):
    a = 2
    sumFact = 0
    while num > 1:
        if num % a == 0:
            sumFact += a
            num = num // a
        else:
            a += 1
    return sumFact
​
def digRoot(num):
    while num > 9:
        num = sum(list(map(int,str(num))))
    return num
​
def smith_type(number):
    if number == 1:
        return 'Not a Smith'
    if factors(number) == number:
        return 'Trivial Smith'
    if digRoot(number) == digRoot(factors(number)):
        if factors(number-1) != number-1:
            if digRoot(number-1) == digRoot(factors(number-1)):
                return 'Oldest Smith'
        if factors(number+1) != number+1:
            if digRoot(number+1) == digRoot(factors(number+1)):
                return 'Youngest Smith'
        return 'Single Smith'
    else:
        return 'Not a Smith'

