
def tp_checker(home):
    days = 500 * home["tp"] // (home["people"] * 57) 
    if days < 14:
        return "Your TP will only last {} days, buy more!".format(days)
    else:
        return "Your TP will last {} days, no need to panic!".format(days)

