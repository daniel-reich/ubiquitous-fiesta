
def get_total_price(groceries):
    return round(sum([i.get('quantity')*i.get('price') for i in groceries]), 1)

