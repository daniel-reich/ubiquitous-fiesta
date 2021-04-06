
def inches_to_feet(inches):
    feet = inches / 12
    if feet < 1 :
        return 0
    return feet
​
​
game = inches_to_feet(14)
print(game)

