
from itertools import product
​
def generate_nonconsecutive(n):
    return " ".join([combo for combo in ["".join(list(combi)) for combi in product("01",repeat=n)] if "11" not in combo])

