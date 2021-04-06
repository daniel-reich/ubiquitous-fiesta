
def journey_distance(n):
    if n == 3:
        return 1
    elif n > 3:
        return ((n-3)/2)+1
    elif n < 3:
        return n/3

