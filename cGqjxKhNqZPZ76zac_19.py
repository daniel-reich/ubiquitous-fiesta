
def fire(matrix, coordinates):
    pos = 'ABCDE'
    mat = {pos[idx]+str(i+1): x for idx, sub in enumerate(matrix) for i, x in enumerate(sub)}
    return 'splash' if mat[coordinates] == '.' else 'BOOM'

