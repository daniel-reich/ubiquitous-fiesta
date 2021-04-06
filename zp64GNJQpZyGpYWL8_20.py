
def score_it(s):
    op, r, j = 0, 0, ""
    for i in s:
        if i == "(":
            if j != "":
                r += op * int(j)
                j = ""
            op += 1
        elif i == ")":
            if j != "":
                r += op * int(j)
                j = ""
            op -= 1
        elif i.isnumeric() and op > 0:
            j += i
    return r

