
def chi_squared_test(data):
    M = [data["E"], data["T"]]
    row_sum1, row_sum2 = sum(M[0]), sum(M[1])
    col_sum1, col_sum2 = M[0][0] + M[1][0], M[0][1] + M[1][1]
    total = row_sum1 + row_sum2
    expected = [[row_sum1 * col_sum1 / total, row_sum1 * col_sum2 / total],
               [row_sum2 * col_sum1 / total, row_sum2 * col_sum2 / total]]
    for i in range(2):
        for j in range(2):
            M[i][j] = (M[i][j] - expected[i][j])**2 / expected[i][j]
    chi_squared = round(sum(M[0]) + sum(M[1]), 1)
    alpha1, alpha5 = 6.635, 3.841
    if chi_squared > alpha1:
        return [chi_squared, "Edabitin effectiveness = 99%"]
    elif chi_squared > alpha5:
        return [chi_squared, "Edabitin effectiveness = 95%"]
    else:
        return [chi_squared, "Edabitin is ininfluent"]

