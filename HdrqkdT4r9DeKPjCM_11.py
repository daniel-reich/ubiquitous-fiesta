
def is_polygonal(n):
    r, b = [], ""
    if n == 1:
        return "0th of all"
    for a in range(3, n + 1):
        x = 0
        while ((a * x * (x + 1) // 2) + 1) < n:
            x += 1
            if ((a * x * (x + 1) // 2) + 1) == n:
                if str(x)[-1] == "1" and x != 11: b = "st"
                elif str(x)[-1] == "2" and x != 12: b = "nd"
                elif str(x)[-1] == "3" and x != 13: b = "rd"
                else: b = "th"
                add = "{}{} {}-gonal number".format(x, b, a)
                r.append(add)
    if r:
        return r 
    return False

