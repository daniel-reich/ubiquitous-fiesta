
def get_products(lst):
    result = []
    for i in range((len(lst))):
        stored_value = lst[i]
        del lst[i]
        product = 1
        for j in lst:
            product *= j
        result.append(product)
        lst.insert(i, stored_value)
    return result

