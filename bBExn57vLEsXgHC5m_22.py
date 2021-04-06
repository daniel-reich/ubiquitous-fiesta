
def same_line(ls: list) -> bool:
    if ls[0][0] == ls[1][0]:
        if ls[0][0] == ls[2][0]:
            return True
        else:
            return False
    a = (ls[0][1] - ls[1][1]) / (ls[0][0] - ls[1][0])
    b = ls[0][1] - a * ls[0][0]
    return ls[2][1] == a * ls[2][0] + b

