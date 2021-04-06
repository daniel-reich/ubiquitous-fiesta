
def matrix_multiply(a, b):
    rows_a, cols_a = len(a), len(a[0]);
    rows_b, cols_b = len(b), len(b[0]);
    if cols_a != rows_b:
        return 'invalid';
​
    result_matrix = []
    
    for r in range(rows_a):
        result_row = []
        for c in range(cols_b):
            row_vals = a[r]
            col_vals = [row[c] for row in b]
            s = sum([l * r for l,r in zip(row_vals, col_vals)])
            result_row.append(s)
        result_matrix.append(result_row)
    return result_matrix

