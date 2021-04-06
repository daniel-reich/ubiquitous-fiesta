
def can_pay_cost(mana_pool, cost):
    '''
    Returns True if there is enough mana in the mana pool to pay the mana cost.
    Constraints and meanings defined in the instructions.
    '''
    mana_pool = list(mana_pool)
    gen_spells = 0  # number of spells which can be fulfilled by any mana
    gen_spells_lst = [item for item in cost if item.isnumeric()]
    if gen_spells_lst:
        gen_spells = int(''.join(gen_spells_lst))
        cost = cost[len(gen_spells_lst):]
​
    for item in cost:
        if item not in mana_pool:
            return False  # can't meet a specific mana requirement
        mana_pool.remove(item)
​
    return len(mana_pool) >= gen_spells  # can meet non specifics?

