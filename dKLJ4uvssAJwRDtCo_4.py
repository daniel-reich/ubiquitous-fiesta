
products = [
{ 'number': 1, 'price': 100, 'name': 'Orange juice' },
{ 'number': 2, 'price': 200, 'name': 'Soda' },
{ 'number': 3, 'price': 150, 'name': 'Chocolate snack' },
{ 'number': 4, 'price': 250, 'name': 'Cookies' },
{ 'number': 5, 'price': 180, 'name': 'Gummy bears' },
{ 'number': 6, 'price': 500, 'name': 'Condoms' },
{ 'number': 7, 'price': 120, 'name': 'Crackers' },
{ 'number': 8, 'price': 220, 'name': 'Potato chips' },
{ 'number': 9, 'price': 80,  'name': 'Small snack' }
]
​
def vending_machine(products, money, product_number):
​
    def changefunct(n):
        for i in coins:
            nonlocal change
            if n // i > 0:
                change += [i] * (n // i)
                n -= (n // i) * i
        return {'product': product_name, 'change': change}
​
    coins = [500, 200, 100, 50, 20, 10]
    change = []
    change_cents = 1
    product_name = str()
​
    for i in products:
        if i['number'] == product_number:
            product_name = i['name']
​
    if product_number not in range(1, 10):
        return 'Enter a valid product number'
    
    for i in products:
        if i['number'] == product_number:
            if money < i['price']:
                return 'Not enough money for this product'
            elif money > i['price']:
                change_cents = money - i['price']
                return changefunct(change_cents)
            else:
                return {'product': product_name, 'change': change}

