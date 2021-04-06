
def dolla_dolla_bills(money):
    a = "${:0,.2f}".format(float(money))
    return a.replace('$-', '-$')

