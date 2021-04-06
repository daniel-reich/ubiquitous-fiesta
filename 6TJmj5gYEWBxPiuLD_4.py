
def seating_students(lst):
    k, *occupied = lst
    pairs = 0
    for i in range(1, k - 2, 2):
        if i not in occupied and i + 1 not in occupied:
            pairs += 1
        if i + 1 not in occupied and i + 3 not in occupied:
            pairs += 1
        if i not in occupied and i + 2 not in occupied:
            pairs += 1
    if i + 2 not in occupied and i + 3 not in occupied:
        pairs += 1
    return pairs

