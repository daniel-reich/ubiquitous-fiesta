
def bill_split(spicy, cost):
    return [
        int(sum(p[1]/2 if p[0] == "N" else p[1] for p in zip(spicy, cost))),
        int(sum(p[1]/2 for p in zip(spicy, cost) if p[0] == "N"))
        ]

