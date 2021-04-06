
import re
ANIMALS = ["muggercrocodile", "one-hornedrhino", "python", "moth", "monitorlizard", "bengaltiger"]
def fauna_number(txt):
    animals = (a.split() for a in re.findall(r'\d+ [a-z\-]+\b', txt))
    return [(a, n) for n, a in animals if a in ANIMALS]

