
def is_shape_possible(n, angles):
    return n>2 and (n-2)*180==sum(angles) and all(i<=180 for i in angles)

