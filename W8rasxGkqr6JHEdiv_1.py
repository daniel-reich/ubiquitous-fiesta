
from itertools import permutations, product
​
def countdown(operands, target):
    for i in permutations(operands, len(operands)):
        for j in product(('+', '-', '*', '//'), repeat=len(operands)):
            eq = ''.join(str(a)+b for a, b in zip(i, j))[:-1]
            if eval(eq.rstrip('/')) == target:
                return eq

