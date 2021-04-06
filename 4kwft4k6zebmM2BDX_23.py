
def chi_squared_test(data):
    original_data = []
    for key, val in data.items():
        original_data.append(val)
    n = len(original_data)
    sum_rows = [sum(row) for row in original_data]
    sum_cols = [sum(col) for col in zip(*original_data)]
    total = sum(sum_rows)
    expected_data = [[sum_cols[c] * sum_rows[r] / total for c in range(n)]
                     for r in range(n)]
    chi_squared = sum((original_data[r][c] - expected_data[r][c]) ** 2
                      / expected_data[r][c]
                      for r in range(n) for c in range(n))
    if chi_squared > 6.635:
        assessment = 'Edabitin effectiveness = 99%'
    elif chi_squared > 3.841:
        assessment = 'Edabitin effectiveness = 95%'
    else:
        assessment = 'Edabitin is ininfluent'
    return [round(chi_squared, 1), assessment]

