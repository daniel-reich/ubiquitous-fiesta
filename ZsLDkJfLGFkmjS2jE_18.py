
def diving_minigame(lst):
    breath=10
    for i in lst:
        if i>=0:
            breath+=4
        if i<=0:
            breath-=2
    return False if breath%4==0 or breath==0 else True

