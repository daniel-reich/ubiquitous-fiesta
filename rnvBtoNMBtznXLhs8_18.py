
def win_round(you,opp):
    x=sorted(you)
    y=sorted(opp)
    m=str(x[-1])+str(x[-2])
    n=str(y[-1])+str(y[-2])
    if m>n:
        return True
    else:
        return False

