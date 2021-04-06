
def dolla_dolla_bills(money):
    return '-$' + '{:,.2f}'.format(abs(money)) if money < 0 else '${:,.2f}'.format(money)

