
overlapping_rectangles = lambda rect1, rect2: max(min(rect1[0] + rect1[2], rect2[0] + rect2[2]) - max(rect1[0], rect2[0]), 0) * max(min(rect1[1] + rect1[3], rect2[1] + rect2[3]) - max(rect1[1], rect2[1]), 0)

