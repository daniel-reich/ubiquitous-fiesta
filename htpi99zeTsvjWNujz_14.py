
def halve_count(a, b):
    if a > b:
        return halve_count(a/2, b) + 1
    return -1

