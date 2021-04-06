
def can_pay_cost(mana_pool, cost):
    mana_pool=list(mana_pool)
    string=("".join([char for char in cost if not char.isalpha()]))
    number=0 if string =="" else int(string)
    for char in cost:
        if char.isalpha():
            if char not in mana_pool:
                return False
            else:
                mana_pool.remove(char)
    return len(mana_pool)>=number

