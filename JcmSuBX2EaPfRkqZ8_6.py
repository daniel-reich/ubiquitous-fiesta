
def get_total_price(groceries):
    return round(sum(dict_1["price"] * dict_1["quantity"] for dict_1 in groceries), 1)

