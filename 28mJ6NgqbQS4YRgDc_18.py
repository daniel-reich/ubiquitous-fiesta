
def can_pay_cost(mana_pool, cost):
    dgt = ''.join(i for i in cost if i.isdigit())
    alp = ''.join(i for i in cost if i.isalpha())
    cst = int(dgt) if len(dgt) > 0 else 0
    for a in alp:
        if a in mana_pool:
            alp = alp.replace(a, '', 1)
            mana_pool = mana_pool.replace(a, '', 1)
        else:
            return False
    rem_c = cst*'1'+alp
    return len(mana_pool) >= len(rem_c)

