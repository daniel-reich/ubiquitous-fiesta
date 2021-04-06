
def product_probability(u):
    total = 1
    for i in range(u):
        total *=  (365-i)
    return total
​
​
def probability(u):
    return round(1- ((product_probability(u)) / (365 ** u)), 2)

