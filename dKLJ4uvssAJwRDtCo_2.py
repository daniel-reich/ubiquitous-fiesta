
def greedy_change(difference):
    coins = [500, 200, 100, 50, 20, 10]
    change = []
    while difference > 0 and len(coins) > 0:
        if coins[0] > difference:
            coins = coins[1:]
        else:
            difference -= coins[0]
            change.append(coins[0])
    return change
            
def vending_machine(products, money, product_number):
    valid = False
    for i in products:
        if i['number'] == product_number:
            name = i['name']
            price = i['price']
            valid = True
            break
    if not valid:
        return 'Enter a valid product number'
    if money < price:
        return 'Not enough money for this product'  
    return {'product' : name, 'change' : greedy_change(money - price)}

