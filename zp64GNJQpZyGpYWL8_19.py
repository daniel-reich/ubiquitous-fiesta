
from re import findall
​
def score_it(s):
    total, depth = 0, 0
    items = findall(r"\)|\d+|\(", s)
    for item in items:
        if item == ")":
            depth -= 1
        elif item.isdigit():
            total += int(item) * depth
        else:
            depth += 1
    return total

