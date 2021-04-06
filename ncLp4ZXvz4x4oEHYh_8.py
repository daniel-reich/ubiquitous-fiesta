
def sum_of_two(a, b, v):
    for n in a:
        for i in b:
            if n + i == v:
                return True
    return False

