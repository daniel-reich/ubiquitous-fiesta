
def get_coin_balances(lst1, lst2):
    first, second = 3, 3
    for m1, m2 in zip(lst1, lst2):
        if m1 == "share":
            first -= 1
            second += 3
        if m2 == "share":
            second -= 1
            first += 3
    return [first, second]

