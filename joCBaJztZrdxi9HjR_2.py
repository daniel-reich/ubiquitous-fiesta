
def tp_checker(home):
    people = home.get("people")
    tp = home.get("tp")
    total_sheet = 500 * tp
    single_day = 57 * people
    net = total_sheet // single_day
    if net > 14:
        return "Your TP will last {} days, no need to panic!".format(net)
    return "Your TP will only last {} days, buy more!".format(net)

