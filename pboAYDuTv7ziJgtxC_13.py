
def min_turns(current, target):
    return sum(min([(int(target[x]) - int(current[x])) % 10, (int(current[x]) - int(target[x])) % 10]) for x in range(len(current)))

