
def vending_machine(products, money, product_number):
    if 0 < product_number < 10:
        price, name = products[product_number-1]['price'], products[product_number-1]['name']
        if price>money:
            return "Not enough money for this product"
        else:
            diff = money-price
            arr = []
            for coin in [500, 200, 100, 50, 20, 10]:
                if diff-coin>=0:
                    arr += int(diff / coin) * [coin]
                    diff -= int(diff / coin) * coin
            return { "product": name, "change": arr }
    else:
        return "Enter a valid product number"

