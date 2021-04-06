
def bill_split(spicy, cost):
    a = list(zip(spicy,cost))
    spicy = sum([b[1] for b in a if b[0] == 'S'])
    ns = sum([b[1] for b in a if b[0] == 'N']) / 2
    return [int(spicy + ns), int(ns)]

