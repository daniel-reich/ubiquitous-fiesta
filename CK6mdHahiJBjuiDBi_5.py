
def can_fit(weights, bags):
    groupsof10 = sum(weights) // 10
    rem = sum(weights) % 10
    if groupsof10 + bool(rem) <= bags:
        return True
    return False

