
def straight_digital(number):
    if number < 100:
        return "Not Straight"
    n = str(number)
    if len(set(n)) == 1:
        return "Trivial Straight"
    diffs = [int(n[i]) - int(n[i-1]) for i in range(1, len(n))]
    return "Not Straight" if len(set(diffs)) != 1 else list(diffs)[0]

