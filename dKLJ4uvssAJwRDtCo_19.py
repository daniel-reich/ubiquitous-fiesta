
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
    if product_number not in range(1,10):
        return "Enter a valid product number"
    if money<products[product_number-1]['price']:
        return 'Not enough money for this product'
    c=[500, 200, 100, 50, 20, 10]
    change_list=[]
    if products[product_number-1]['price']<money:
        change_total=(money-products[product_number-1]['price'])
        
        while change_total:
            for x in range(len(c)):
                if c[x]>change_total:
                    c[x]=0   
            change_list.append(max(c))
            change_total-=max(c)
            
    return {'product':products[product_number-1]['name'],"change":change_list}

