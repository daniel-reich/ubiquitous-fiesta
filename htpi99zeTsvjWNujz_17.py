
def halve_count(a, b):
    counter = 0
    while a > b:
        a = a / 2
        counter += 1
    return counter-1

