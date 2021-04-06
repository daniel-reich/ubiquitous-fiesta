
def max_product(lst):
    products=[]
    for i in range(len(lst)):
        for i1 in range(len(lst)):
            for i2 in range(len(lst)):
                if i!=i1 and i1!=i2 and i!=i2:
​
                
                    products.append(lst[i]*lst[i1]*lst[i2])
​
    return max(products)
​
​
​
def min_product(lst):
    products = []
    for i in range(len(lst)):
        for i1 in range(len(lst)):
            for i2 in range(len(lst)):
                if i != i1 and i1 != i2 and i != i2:
                    products.append(lst[i] * lst[i1] * lst[i2])
​
    return min(products)

