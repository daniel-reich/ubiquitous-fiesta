
def dice_game(lst):
    sum = 0
    for a,b in lst:
        if a == b:
            return 0
        else:
            sum += a+b
​
    return sum

