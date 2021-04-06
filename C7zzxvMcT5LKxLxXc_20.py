
def decode(txt):
    return [c - 9*((c>99) +c//10) for c in map(ord, txt)]

