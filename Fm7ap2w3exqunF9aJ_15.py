
def count_lone_ones(n):
    n = str(n)
    for x in range(len(n), 1, -1):
        n = n.replace(x * "1", "_")
    return n.count("1")

