
def is_prime(number):
    if number <= 1:
        return False
    for x in range(2, number):
        if not number % x:
            return False
    return True
​
def how_bad(num):
    l = []
    binary = "{0:b}".format(num)
    if int(binary.count('1'))%2 == 0:
        l.append('Evil')
    if int(binary.count('1'))%2 == 1:
        l.append('Odious')
    if is_prime(int(binary.count('1'))):
        l.append('Pernicious')
    return l

