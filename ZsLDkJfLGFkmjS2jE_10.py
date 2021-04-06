
def diving_minigame(lst):
    i = 10
    for j in lst:
        if j<0:i-=2
        else:i+=4
        if i==0:return False
        if i>10:i=10
    return True

