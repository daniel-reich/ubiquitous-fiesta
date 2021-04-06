
def risiko(attacker, defender):
    attack = sorted(attacker, reverse=True)
    defend = sorted(defender, reverse=True)
    return sum(
        a > d
        for a, d in zip(attack, defend)
    )

