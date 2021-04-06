
import math
def who_wins_tonight(coins, space, price, size):
    will_space = space / size
    bill_coins = coins / price
        
    will_space_value = math.floor(will_space)
    bill_coins_value = math.floor(bill_coins)
        
    if(will_space_value == bill_coins_value):
        return "Tie"
    elif(will_space_value > bill_coins_value):
        return "Will"
    elif(will_space_value < bill_coins_value):
        return "Bill"

