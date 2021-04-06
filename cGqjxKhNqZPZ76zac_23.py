
def fire(matrix, c):
    return 'splash' if matrix['ABCDE'.index(c[0])][int(c[1])-1] == '.' else 'BOOM'

