
def sum_odd_and_even(lst):
​
    evens = []
    odds = []
    
    for value in lst:
        if value %2 == 0:
            evens.append(value)
        else:
            odds.append(value)
    
    return[sum(evens), sum(odds)]

