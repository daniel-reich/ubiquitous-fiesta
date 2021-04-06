
from math import factorial
​
​
lengths = []
​
​
def flatten(lst):
    global lengths
    for i in lst:
        if type(i) == list:
            lengths.append(len(i))
            flatten(i)
​
​
def nespers(lst):
    global lengths
    lengths.clear()
    lengths.append(len(lst))
    flatten(lst)
    result = 1
    for i in lengths:
        result *= factorial(i)
    return result

