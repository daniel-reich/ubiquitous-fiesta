
def same_line(lst):
    left, mid, right = (complex(*pair) for pair in sorted(lst))
    return not ((mid -left)/(right -left)).imag

