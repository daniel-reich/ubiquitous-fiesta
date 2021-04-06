
def is_prob_matrix(arr):
    if len(arr) != len(arr[0]):
        return False
    for row in arr:
        tot = 0
        for item in row:
            tot += item
            if not (0 <= item <= 1):
                return False
        if tot != 1:
            return False
    return True

