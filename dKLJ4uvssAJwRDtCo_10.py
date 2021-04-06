
import math
​
def vending_machine(products, money, product_number):
    if product_number > 9 or product_number < 1: return "Enter a valid product number"
​
    item = list(products[product_number - 1].values())[2]
    price = list(products[product_number - 1].values())[1]
​
    if int(money) < price: return "Not enough money for this product"
​
    remain = money - price
    currency = [500, 200, 100, 50, 20, 10]
    change = []
    for i in range(0,6):
        if remain >= currency[i]:
            coins = (math.floor(remain/currency[i]))
            remain = remain - (coins * currency[i])
            change += [currency[i]] * coins
​
    return {"product": item, "change": change}

