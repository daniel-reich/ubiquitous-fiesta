
def is_fact(n):
    total = 1
    start = 1
    while total <= n:
        total = total * start
        start = start + 1
        if total == n:
            return True
    return False
​
def filter_factorials(numbers):
    return list(filter(is_fact,numbers))

