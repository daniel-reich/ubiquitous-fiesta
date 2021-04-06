
def over_twenty_one(lst):
    newlst = []
    for x in lst:
        x = str(x)
        if x.isdigit():
            newlst.append(int(x))
        elif x.isalpha():
            if x == "J" or x == "K" or x == "Q":
                newlst.append(10)
            elif x == "A":
                newlst.append(1)
    if sum(newlst) > 21:
        return True
    return False

