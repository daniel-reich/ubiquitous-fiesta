
def dice_roll(num, out):
    if num == 1:
        if out <= 0 or out > 6:
            return 0
        else:
            return 1
    total = 0
    for i in range(1,7):
        temp = dice_roll(num-1, out-i)
        total += temp
    
    return total

