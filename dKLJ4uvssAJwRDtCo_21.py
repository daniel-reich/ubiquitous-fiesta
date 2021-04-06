
def vending_machine(products, money, product_number):
    coins = [500, 200, 100, 50, 20, 10]
    result = {'product': "", 'change': []}
    if product_number not in range(1, 11):
        return 'Enter a valid product number'
    for product in products:
        if product['number'] == product_number:
            result['product'] = product['name']
            if money < product['price']:
                return 'Not enough money for this product'
            else:
                change = money - product['price']
                while change != 0:
                    for coin in coins:
                        if change - coin < 0:
                            continue
                        elif change - coin == 0:
                            result['change'].append(coin)
                            change -= coin
                            break
                        else:
                            result['change'].append(coin)
                            change -= coin
                            break
    return result

