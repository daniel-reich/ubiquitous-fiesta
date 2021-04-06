
def overlapping_rectangles(rect1, rect2):
    a = min(rect1[0] + rect1[2],rect2[0] + rect2[2]) - rect2[0]
    b = min(rect1[1] + rect1[3],rect2[1] + rect2[3]) - max(rect1[1],rect2[1]) 
    return a * b if a > 0 and b > 0 else 0

