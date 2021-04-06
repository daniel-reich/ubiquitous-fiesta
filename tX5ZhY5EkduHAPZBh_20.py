
def nearest_element(n, lst):
    nearest = {}
    difference = abs(lst[0] - n)
    index = 0
    for element in lst:
        if abs(element - n) < difference:
            nearest = {element: index}
            difference = abs(element - n)
        elif abs(element - n) == difference:
            nearest[element] = index
        index += 1
    return nearest[max(nearest.keys())]

