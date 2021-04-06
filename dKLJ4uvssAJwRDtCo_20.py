
def vending_machine(products, money, product_number):
    change = [500, 200, 100, 50, 20, 10]
​
    for x in products:
        if x['number'] == product_number:
            name = x['name']
            price = x['price']
            break
    else:
        return 'Enter a valid product number'
    
    if money < price: return 'Not enough money for this product'
    
    required = money - price
    change_set = []
    while required:
        for i in change:
            if required  >= i:
                change_set.append(i)
                required -= i
                break
    
    return {'product': name, 'change': change_set}

