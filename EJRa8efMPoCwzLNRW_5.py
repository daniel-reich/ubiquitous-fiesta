
from re import search, sub
def dakiti(s):
    return " ".join(sub(r"\d", "", word) for word in
                    sorted(s.split(), key=lambda w: search(r"\d", w).group()))

