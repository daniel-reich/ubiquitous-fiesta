
def is_autobiographical(n):
    n = str(n)
    if len(n) > 10:
        return False
    else:
        lst = []
        for i in range(0, len(n)):
            lst.append(int(n[i]) == n.count('{}'.format(i)))
        return all(lst)

