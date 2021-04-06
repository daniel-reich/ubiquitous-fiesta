
def has_valid_price(product):
    if not product:
        return False
    if 'product' not in product:
        return False
    if 'price' not in product:
        return False
    if type(product['price']) not in (int, float):
        return False
    return product['price'] >= 0

