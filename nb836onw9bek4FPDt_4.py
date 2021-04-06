
def count_same_ends(txt):
    count = 0
    a = "".join([i.lower() for i in txt if i.isalpha() or i.isspace()]).split()
    for i in a:
        if len(i) > 1 and i[0] == i[-1]:
            count += 1
    return count

