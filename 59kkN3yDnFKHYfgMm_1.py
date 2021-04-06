
from re import search
def best_friend(txt, a, b):
    return not bool(search(r"{0}[^{1}]|{0}$".format(a, b), txt))

