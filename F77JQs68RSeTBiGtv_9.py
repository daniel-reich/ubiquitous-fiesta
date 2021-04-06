
def diamond_sum(num):
    halfNum = num // 2
    
    total = 0
    
    for r in range(num):
        startingValue = r * num + 1
        if r == 0 or r == num - 1:
            total += startingValue + halfNum
            continue
        delta = r // 2 + 1
        total += (startingValue + halfNum + delta)
        total += (startingValue + halfNum - delta)
    return total

