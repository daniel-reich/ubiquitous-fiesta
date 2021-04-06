
def bowling(pins):
    score = 0
    for _ in range(1, 11):
        b1 = pins.pop(0)
        score += b1 + (sum(pins[:2]) if b1 == 10 else 0)
        if b1 < 10:
            b2 = pins.pop(0)
            score += b2 + (pins[0] if b1 + b2 == 10 else 0)
    return score

