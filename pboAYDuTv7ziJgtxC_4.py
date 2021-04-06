
def min_turns(current, target):
    diffs = [(int(a)-int(b))%10 for a, b in zip(current, target)]
    return sum(min(dif, 10-dif) for dif in diffs)

