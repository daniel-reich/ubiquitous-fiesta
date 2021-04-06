
def score31(*args):
    set_val = set(card[-1] for card in args)
    if len(set_val) == 1:
        if set_val == {"A"}:
            return 32
        return 30.5
​
    suit = {"H": 0, "C": 0, "S": 0, "D": 0}
    face = {"A": 11, "K": 10, "Q": 10, "J": 10}
    for card in args:
        value = card[1:]
        if value in face:
            suit[card[0]] += face[value]
        else:
            suit[card[0]] += int(value)
    return max(suit.values())

