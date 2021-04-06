
def hanoi(disk, source=1, dest=3, aux=2, res=None):
    if disk == 0:
        return []
    if res is None:
        res = []
    if disk == 1:
        res.append((source, dest))
    else:
        hanoi(disk - 1, source, aux, dest, res)
        res.append((source, dest))
        hanoi(disk - 1, aux, dest, source, res)
    return res

