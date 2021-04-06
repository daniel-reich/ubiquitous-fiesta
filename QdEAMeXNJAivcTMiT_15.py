
def boxes(weights):
    count = 0
    while weights:
        idx = 1
        while idx < len(weights) and sum(weights[:idx + 1]) <= 10:
            idx += 1
        count += 1
        weights = weights[idx:]
    return count

