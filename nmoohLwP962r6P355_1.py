
def straight_digital(n):
    if n < 100:
        return 'Not Straight'
    s = str(n)
    if len(set(s)) == 1:
        return 'Trivial Straight'
    diff = [int(b) - int(a) for a, b in zip(s, s[1:])]
    if len(set(diff)) != 1:
        return 'Not Straight'
    return diff[0]

