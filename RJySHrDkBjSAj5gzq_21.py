
def factorial(n):
    if n == 1 or n == 2:
        return n
    else:
        return n * factorial(n-1)
​
​
def nespers(lst):
    if len(lst) == 0:
        return 1
    elif all(type(item) != list for item in lst):
        return factorial(len(lst))
    else:
        result = factorial(len(lst))
        for item in lst:
            if type(item) == list:
                result *= nespers(item)
        return result

