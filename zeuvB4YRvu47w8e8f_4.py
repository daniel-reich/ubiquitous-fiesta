
def full_cycle(lst):
    if set(lst) != set(range(len(lst))):
        return False
    cycle = [lst[0]]
    for _ in range(len(lst) - 1):
        cycle.append(lst[cycle[-1]])
    return sorted(lst) == sorted(cycle)

