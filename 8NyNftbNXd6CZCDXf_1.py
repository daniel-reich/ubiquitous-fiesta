
def get_coin_balances(lst1, lst2):
    red, green = 3, 3
    for k in range(len(lst1)):
        if lst1[k] == "share":
            green -= 1
            red += 3
        if lst2[k] == "share":
            red -= 1
            green += 3
    return [green, red]

