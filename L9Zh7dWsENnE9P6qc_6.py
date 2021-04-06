
def josephus(people):
    if people == 1:
        return 1
    p = {i: True for i in range(people)}
    alive = people
    cur = 0
    while alive > 1:
        cur = (cur + 1) % people
        while not p[cur]:
            cur = (cur + 1) % people
        p[cur] = False
        alive -= 1
        while not p[cur]:
            cur = (cur + 1) % people
    return [k+1 for k, v in p.items() if v][0]

