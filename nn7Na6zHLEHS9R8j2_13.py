
def deep_count(lst):
    counter = 0
    for item in lst:
        counter += 1
        if type(item) == list:
            counter += deep_count(item)
​
    return counter

