
def dice_score(throw):
    x = 0
    if throw.count(1) >= 3:
        x += 1000
    if throw.count(1) >= 1:
        x +=  100
    if throw.count(2) >= 3:
        x += 200
    if throw.count(3) >= 3:
        x += 300
    if throw.count(4) >= 3:
        x += 400
    if throw.count(5) >= 3:
        x += 500
    if throw.count(5) >= 1:
        x += 50
    if throw.count(6) >= 3:
        x += 600
    return x
​
​
print(dice_score([2, 4, 4, 5, 4]))

