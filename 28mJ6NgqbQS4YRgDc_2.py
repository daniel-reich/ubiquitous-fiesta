
def can_pay_cost(mana, cost):
    for i in cost:
        if i in mana:
            mana = mana.replace(i, '', 1)
            cost = cost.replace(i, '', 1)
    if not cost:
        return True
    if cost.isdigit():
        return len(mana) >= int(cost)
    return False

