
def over_twenty_one(cards):
    num = 0
    for i in cards:
        if type(i)==str and not i == "A":
            num+=10
        elif type(i)==str:
            if num == 20:
                num+=1
            elif num == 1:
                num+=20
        else:
            num+=i
    return num>21

