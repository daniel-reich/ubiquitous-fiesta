
def interview(lst, tot):
    m = [5, 5, 10, 10, 20, 20, 40, 40]
    a = all([y <= x for x, y in zip(m, lst)])
    b = len(lst) == 8
    c =  tot <= 120
    if a and b and c:
        return "qualified"
    return "disqualified"

