
def bracket_logic(xp):
    opening = "({[<"
    closing = ">]})"
    dc = {">":"<","]":"[","}":"{",")":"("}
    d = []
    for i in xp:
        if i in opening:
            d.append(i)
        elif i in closing:
            if d[-1] != dc[i]:
                return False
            d.pop()
    if len(d) > 0:
        return False
    else:
        return True

