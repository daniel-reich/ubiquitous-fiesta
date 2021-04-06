
def left_slide(row):
    left = [x for x in row if x != 0]
    i = 0
    while i + 1 < len(left):
        if left[i] == left[i + 1]:
            left[i] = left[i] + left[i + 1]
            left.pop(i + 1)
        i += 1
    left = left + [0] * (len(row) - len(left))    
    return left

