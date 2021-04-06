
def dice_roll(n,m):
    if n==1:
        return 1 if 1<=m<=6 else 0
    if n>m:
        return 0
    return sum([dice_roll(n-1,m-x) for x in range(1,7)])

