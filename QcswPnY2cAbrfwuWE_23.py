
def is_factorial(num):
    if num == 1:
        return True
    start = 2
    while num > 1:
        if num % start != 0:
            return False
        num = num // start
        start = start + 1
    return True
​
​
def filter_factorials(numbers):
    return [n for n in numbers if is_factorial(n)]

