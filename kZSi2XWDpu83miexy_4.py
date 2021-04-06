
from itertools import permutations
def post_fix(expr):
    for p in permutations(expr.split(" ")):
        try:
            if eval(" ".join(p)) == int(eval(" ".join(p))):
                return int(eval(" ".join(p)))
        except:
            pass

