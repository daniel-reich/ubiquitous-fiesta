
def is_magic(square):
    if square == []:
        return True
    m = sum(square[0])
    for row in square[1:]:
        if sum(row) != m:
            return False
    square = [list(i) for i in zip(*square)]
    for row in square:
        if sum(row) != m:
            return False
    k = len(square)
    if sum([square[i][i] for i in range(k)]) != m:
        return False
    if sum([square[i][k-1-i] for i in range(k)]) != m:
        return False
    nums = []
    for row in square:
        nums += row
    return sorted(nums) == list(range(1, len(square)**2 + 1))

