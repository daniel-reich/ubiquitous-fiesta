
def sum_of_two(a, b, v):
    for num in a:
        if abs(num - v) in b:
            return True
        else:
            continue
    return False

