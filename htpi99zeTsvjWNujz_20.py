
def halve_count(a, b):
    return -1 if a<=b else 1 + halve_count(a/2, b)

