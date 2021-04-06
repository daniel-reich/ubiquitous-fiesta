
def most_expensive_item(products):
    for k, v in products.items():
        if v is max(products.values()):
            return k

