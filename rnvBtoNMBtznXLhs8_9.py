
def win_round(you, opp):
    you.sort(reverse=True)
    opp.sort(reverse=True)
    if int(str(you[0])+str(you[1])) > int(str(opp[0])+str(opp[1])):return True
    return False

