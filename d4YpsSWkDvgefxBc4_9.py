
def over_twenty_one(cards):
    total = 0
    maximum = 21
    for i in range(len(cards)):
        if cards[i] == 'J' or cards[i] == 'Q' or cards[i] == 'K':
            total = total + 10
        elif cards[i] == 'A' :
            pass
​
        else:
            total = total + cards[i]
​
​
    a = cards.count('A') 
    for j in range(a):
        if total > 10:
            total += 1
        else:
            total += 11
    
    if total >21:
        return True
    else:
        return False

