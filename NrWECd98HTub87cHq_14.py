
def overlapping_rectangles(rect1, rect2):
    area = 0
    for x in range(rect1[0], rect1[0] + rect1[2]):
        for y in range(rect1[1], rect1[1] + rect1[3]):
            if (rect2[0] <= x < rect2[0] + rect2[2] and
                    rect2[1] <= y < rect2[1] + rect2[3]):
                area += 1
    return area

