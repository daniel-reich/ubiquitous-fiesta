
win_round =  lambda you, opp : "".join(map(str,sorted(you,reverse=True)[0:2])) > "".join(map(str,sorted(opp,reverse=True)[0:2]))

