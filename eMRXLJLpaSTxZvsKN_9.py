
def is_ladder_safe(ldr):
    ldr = ldr[1:-1]
    rung = [x for x in range(len(ldr)) if ldr[x] == len(ldr[0]) * '#']
    if not rung: return False
    diff = rung[1] - rung[0]
    return all(y-x == diff for x, y in zip(rung, rung[1:])) and diff <= 3 and diff * len(rung) >= len(ldr) and len(ldr[0]) >= 5

