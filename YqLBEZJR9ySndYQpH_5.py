
def staircase(n):
    r = []
    for x in range(1, abs(n) + 1):
        r += ["_" * (abs(n) - x) + "#" * x] 
    if n < 0:
        r = reversed(r)
    return "\n".join(r)

