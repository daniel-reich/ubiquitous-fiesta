
def smallest(digits, value):
​
    n = int("1" + "0" * (digits - 1))
​
    while n % value != 0:
        n += 1
​
    return n

