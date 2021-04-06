
def vending_machine(products, money, product_number):
    dict = {}
    lst = []
    product_name = products[product_number - 1].get('name')
    product_price = products[product_number - 1].get('price')
    change = []
    price_difference = money - product_price
    coins = [500, 200, 100, 50, 20, 10]
    change_list = []
    for i in coins:
        while price_difference >= i:
            change_list.append(i)
            price_difference -= i
    if product_number > 0 and product_number < len(products) + 1:
        dict['product'] = product_name
        if money >= product_price:
            dict['change'] = change_list
            return dict
        else:
            return "Not enough money for this product"
    else:
        return "Enter a valid product number"

