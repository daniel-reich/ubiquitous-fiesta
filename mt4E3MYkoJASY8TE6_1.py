
from itertools import product
d = {"0": "08", "1": "124", "2": "1235", "3": "236", "4": "1457",
     "5": "24568", "6": "3569", "7": "478", "8": "57890", "9": "689"}
def crack_pincode(pincode):
    return sorted("".join(p) for p in product(*[d[c] for c in pincode]))

