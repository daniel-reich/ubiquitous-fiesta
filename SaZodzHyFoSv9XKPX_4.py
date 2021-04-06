
from re import sub
def domino_chain(dominos):
    return sub(r"^[|]+", lambda m: r"/" * len(m.group()), dominos)

