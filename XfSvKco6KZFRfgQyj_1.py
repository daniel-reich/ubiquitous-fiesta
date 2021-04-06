
def find_a_seat(n, lst):
    n //= len(lst)
    for i, k in enumerate(lst):
        if k / n <= 0.5:
            return i
    return -1

