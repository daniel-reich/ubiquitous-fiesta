
def add_bill(money):
    return sum([int(x[1:]) for x in money.replace('k', '000').split(',') if x[0] == 'd'])

