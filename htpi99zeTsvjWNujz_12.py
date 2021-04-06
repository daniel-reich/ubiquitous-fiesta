
def halve_count(a, b,counter = 0):
    a = a / 2
    counter += 1
    return counter - 1 if a <= b else halve_count(a,b) + counter

