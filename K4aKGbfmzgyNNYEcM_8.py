
def is_shape_possible(n, angles):
    return all([num<180 for num in angles]) and sum(angles)==(n-2)*180

