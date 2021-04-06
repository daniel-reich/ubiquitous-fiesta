
def risiko(attacker, defender):
    attacker = sorted(attacker)[::-1]
    defender = sorted(defender)[::-1]
    lst= []
    for x,y in zip(attacker, defender):
        lst.append(x-y)
                   
    adjust = [-1 if num ==0 else 1 if num>0 else -1 for num in lst]
    n = sum(adjust)
    if n <0:
        return 0
    else:
        return n

