
def most_expensive_item(products):
    for k,v in products.items():
        if v == max(products.values()):
            return k

