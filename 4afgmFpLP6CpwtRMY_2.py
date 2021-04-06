
def sudoku_validator(x):
    for i in range(len(x)):
        row = x[i]
        col = [r[i] for r in x]
        if len(row) != len(set(row)) or len(col) != len(set(col)): return False
​
    for i in range(len(x) // 3):
        ans = []
        for j in range(0, len(x)):
            ans.extend(x[j][i * 3:i * 3 + 3])
            if j % 3 == 2 and j > 0:
                if len(ans) != len(set(ans)): return False
                ans = []
    return True

