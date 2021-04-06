
from re import findall
def find_vertex(eq):
    a, b = map(int, findall(r"[+-]*\d+(?=x)", eq))
    return round(-b / a / 2 - 0.001)

