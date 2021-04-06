
def total_volume(*boxes):
    l = 0
    for i in boxes:
        result = 1
        for j in i:
            result *= j
        l += result
    return l

