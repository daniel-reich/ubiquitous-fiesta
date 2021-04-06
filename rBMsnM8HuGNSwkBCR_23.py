
def add_bill(money):
    dollars = [d for d in money.split(',') if d.startswith('d')]
    return sum(int(d[1:-1]) * 1000 if d.endswith('k') else int(d[1:]) for d in dollars)

