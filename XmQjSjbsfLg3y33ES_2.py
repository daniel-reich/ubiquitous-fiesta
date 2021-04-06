
def legalbacklog(time, ope):
    lst, total =list(time.values()), 0
    while lst:
        if len(lst) <= ope: return total+lst[0]
        total += 1
        for i in range(ope):
            if lst[i] == 1:
                lst = lst[:-(ope-i)]
                break
            lst[i] -= 1
        x = max(len(lst), 2 * ope - 1)
        lst = sorted(lst[:x], reverse=True)+lst[x:]
    return total

