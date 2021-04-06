
from itertools import permutations
lst_ops = ["+", "-", "*", "/"]
def simple_equation(a, b, c):
    for x, y, z in permutations([a, b, c]):
        for o in lst_ops:
            eq = "{}{}{}=={}".format(x, o, y, z)
            if eval(eq):
                return eq.replace("==", "=")
    return ""

