
def has_valid_price(product):
    if not product:
        return False
    try:
        return (isinstance(product["price"], int) or isinstance(product["price"], float)) and product["price"] >= 0
    except KeyError:
        return False

