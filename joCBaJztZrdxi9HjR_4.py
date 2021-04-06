
def tp_checker(home):
    sheets_per_roll = 500  # number of sheets in an average TP roll
    avg_use = 57  # average use of sheets/person/day
​
    people = home["people"]
    sheets = home["tp"] * sheets_per_roll
    days = sheets // (avg_use * people)
​
    if days <= 14:
        return "Your TP will only last {} days, buy more!".format(days)
​
    else:
        return "Your TP will last {} days, no need to panic!".format(days)

