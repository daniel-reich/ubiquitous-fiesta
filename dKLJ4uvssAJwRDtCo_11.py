
def vending_machine(products, money, product_number):
​
    def make_change(change):
        coins = [500, 200, 100, 50, 20, 10]
        change_coins = []
        for coin in coins:
            for item in range(change // coin):
                change_coins.append(coin)
            change = change % coin
        return change_coins
​
    if product_number < 1 or product_number > len(products):
        return "Enter a valid product number"
    product = products[product_number - 1]
    change = money - product['price']
    if change < 0:
        return "Not enough money for this product"
    return {"product" : product['name'], "change": make_change(change)}

