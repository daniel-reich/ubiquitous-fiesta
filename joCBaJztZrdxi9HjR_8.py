
def tp_checker(home):
    days = int(home['tp'] * 500 / home['people'] // 57)
    a = 'only ' if days<14 else ''
    b = 'buy more' if days<14 else 'no need to panic'
    return "Your TP will {}last {} days, {}!".format(a, days, b)

