
def find_a_seat(n, lst):
    cap = n / len(lst)
    for i, x in enumerate(lst):
        if x / cap <= .5:
            return i
    return -1

