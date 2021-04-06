
def get_products(lst):
    
    result = []
    for x in lst:
        num = 1
        a = lst.index(x)
        lst.remove(x)
        for y in lst:
            num *= y
        result.append(num)
        lst.insert(a, x)
    return result

