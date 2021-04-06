
def complete_bracelet(lst):
    pos = []
    l = len(lst)
    for i in range(2,l):
        if l % i == 0:
            pos.append(i)
    if len(pos) == 0:
        return False
    for item in pos:
        if lst[:l//item] == lst[l//item:2*(l//item)]:
            return True
    return False

