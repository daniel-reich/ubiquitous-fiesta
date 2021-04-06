
def win_round(you, opp):
    return int(''.join([str(a) for a in sorted(you, reverse=True)[:2]])) > int(''.join([str(a) for a in sorted(opp, reverse=True)[:2]]))

