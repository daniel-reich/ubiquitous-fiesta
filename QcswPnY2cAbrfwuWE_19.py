
def is_fact(n, i = 2):
    if n == 1: return True
    n, r = divmod(n, i)
    return False if r else is_fact(n, i + 1)
​
def filter_factorials(numbers):
    return list(filter(is_fact, numbers))

