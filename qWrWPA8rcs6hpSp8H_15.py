
def determinant(a):
    if len(a) == 1:
        return a[0][0]
    return sum((-1) ** i * a[0][i]
               * determinant([row[:i] + row[i + 1:] for row in a[1:]])
               for i in range(len(a)))

