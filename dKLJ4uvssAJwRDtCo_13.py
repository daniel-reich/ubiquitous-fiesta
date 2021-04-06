
def vending_machine(products, money, product_number):
​
    chosen_prod = None
    
    for prod in products:
        if product_number == prod['number']:
            chosen_prod = prod # chosen_product is a dictionary containing product info
    
    if chosen_prod == None:
        return 'Enter a valid product number'
    
    if money < chosen_prod['price']:
        return 'Not enough money for this product' 
    
    coins = [500, 200, 100, 50, 20, 10]
    
    change_amount = money - chosen_prod['price']
    
    change_coins = []
    
    num_coins = 0
    
    for coin in coins:
        num_coins = change_amount//coin
        
        for i in range(num_coins):
            change_coins.append(coin)
            
        change_amount -= num_coins*coin
            
    return {'product': chosen_prod['name'], 'change': change_coins }

