
def sudoku_validator(lst: list) -> bool:
    k, box_score = len(lst), sum(range(1, 10))
    # checking rows
    if sum(0 if len(set(i)) != k or sum(i) != box_score else 1 for i in lst) != k:
        return False
​
    # checking columns
    transformed = list(zip(*lst))
    if sum(0 if len(set(i)) != k or sum(i) != box_score else 1 for i in transformed) != k:
        return False
​
    # checking boxes 3x3
    n = k // 3
    for i in range(n):
        for j in range(n):
            sub_L = []
            sub_L.extend(lst[3*i][3*j:3*(j+1)])
            sub_L.extend(lst[3 *i+1][3*j:3*(j + 1)])
            sub_L.extend(lst[3 *i+2][3 * j:3*(j + 1)])
            if sum(sub_L) != box_score:
                return False
    return True

