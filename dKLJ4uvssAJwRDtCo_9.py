
def generate_result_structure(name,chane_list):
    return { 'product': name, 'change': chane_list }
    
def make_change(remainder,coins):
    """Calculate the coins required to make change equal to amount."""
    counts = [0 for _ in coins]
    result = []
    for index, amount in enumerate(coins):     
        #print("index {0}".format(index))
        #print(remainder // amount)
        counts[index] = remainder // amount
        #remainder %= amount
        remainder -= counts[index] * amount
        #print(remainder)
        for i in range(counts[index]):
            result.append(amount)
        
    #print(result)
    return result
​
def vending_machine(products, money, product_number):
    coins = [500, 200, 100, 50, 20, 10]
    result = []
    
    # assign product price & name and validate the inputs
    filtered_list = [x for x in products if x['number']==product_number]
    if len(filtered_list) != 1 :
        return 'Enter a valid product number'
    price = filtered_list[0]['price']
    if money < price:
        return 'Not enough money for this product'
        
    total_coins_to_return = money - price
    print(total_coins_to_return)
    name = filtered_list[0]['name']
    if total_coins_to_return == 0:
        return generate_result_structure(name,[])
    
    #calculate change
    if total_coins_to_return in coins:
        return generate_result_structure(name,[total_coins_to_return])    
    
    change_result  =make_change(total_coins_to_return,coins)
    return generate_result_structure(name,change_result)

