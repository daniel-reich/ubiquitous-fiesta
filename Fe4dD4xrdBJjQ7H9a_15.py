
def who_wins_tonight(coins, space, price, size):
    amount_bill = coins//price
    
    amount_will = space//size
    
    if amount_bill > amount_will:
        return "Bill"
    
    elif amount_will > amount_bill:
        return "Will"
    
    else:
        return "Tie"

