
def boxes(items):
    boxes = 0
    weight = 0
    for item in items:
        if item + weight <= 10:
            weight += item
        else:
            weight = item
            boxes += 1
    return boxes if weight == 0 else boxes + 1

