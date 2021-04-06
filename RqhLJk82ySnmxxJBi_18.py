
def power_morphic(num):
    x = 0
    y = len(str(num))
    z = ""
    for i in range(2,11):
        if num ** i % (10**y) == num:
            x += 1
    if x == 9:
        z = "Polymorphic"
    elif x == 4:
        z = "Quadrimorphic"
    elif x == 2:
        z = "Dimorphic"
    elif x == 1:
        z = "Enamorphic"
    else:
        z = "Amorphic"
        
    return z

