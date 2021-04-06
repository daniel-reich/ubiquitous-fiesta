
def is_magic(square):
    if not square:
        return True
    
    size = len(square)
    rows = [sum(i) for i in square]
    cols = [sum(i) for i in zip(*square)]
    dia1 = sum(square[i][i] for i in range(size))
    dia2 = sum(square[i][-i-1] for i in range(size))
    sum_check = len(set(rows + cols + [dia1] + [dia2])) == 1
    num_check = sorted(set(sum(square, []))) == list(range(1, size**2 + 1))
​
    return sum_check and num_check

