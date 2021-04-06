
def win_round(you, opp):
    you = sorted(you, reverse=True)
    opp = sorted(opp, reverse=True)
    you = you[0] * 10 + you [1]
    opp = opp[0] * 10 + opp [1]
    if you > opp:
        return True
    else:
        return False

