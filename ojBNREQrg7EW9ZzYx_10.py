
def count_eatable_chocolates(money_, cost_):
    money, cost = "", ""
    for i in money_:
        if i.isnumeric():
            money += i
    p_1 = money_.find(money)
    if p_1 > 0 and money_[p_1-1] == "-" or int(money) <= 0:
        return "Invalid Input"
    money = int(money)
    for i in cost_:
        if i.isnumeric():
            cost += i
    p_2 = cost_.find(cost)
    if p_2 > 0 and cost_[p_2-1] == "-" or int(money) <= 0:
        return "Invalid Input"
    cost = int(cost)
    poop, stock =  0, 0
    while money >= cost:
        eat = money // cost
        poop += eat
        wrappers = eat + stock
        money = money - eat * cost + wrappers // 3 * cost
        stock = wrappers % 3
    return poop

