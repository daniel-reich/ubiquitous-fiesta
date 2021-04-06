
def count_same_ends(txt):
    count = 0
    for x in txt.split():
        if len(x) == 1:
            continue
        if x[-1] in [",", "!", "?", "."]:
            x = x[: -1]
        if x.lower()[0] == x.lower()[-1]:
            count += 1
    return count

