
def is_shape_possible(n, angles):
    if max(angles)>180 or min(angles)<1 or n<3:return False
    return (n-2)*180 == sum(angles)

