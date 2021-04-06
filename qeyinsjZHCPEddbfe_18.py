
def dice_game(lst):
    s=0
    for i in lst:
        if i[0]!=i[1]:
            
            s+=i[0]+i[1]
        else:
            return 0
    return s

