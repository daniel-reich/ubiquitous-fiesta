
def maximum_seating(lst):
    s = "00{}00".format("".join(map(str, lst)))
    return sum((len(p) - 2) // 3 for p in s.split("1") if len(p) > 1)

