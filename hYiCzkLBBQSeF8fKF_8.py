
def count(deck):
    a = 0
    for i in deck:
        if i in (2, 3, 4, 5, 6):
            a += 1
        elif i in (10, "J", "Q", "K", "A"):
            a -= 1
    return a

