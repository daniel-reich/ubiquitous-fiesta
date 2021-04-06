
def classify_rug(pattern):
    def trasposed(matrix):
        return list(zip(*matrix))
    def horizontally_symmetrical(matrix):
        return matrix == matrix[::-1]
    def vertically_symmetrical(matrix):
        return horizontally_symmetrical(trasposed(matrix))
    def perfectly_symmetrical(matrix):
        return vertically_symmetrical(matrix) and horizontally_symmetrical(matrix)
    if horizontally_symmetrical(pattern):
        if vertically_symmetrical(pattern):
            return 'perfect'
        else:
            return 'horizontally symmetric'
    elif vertically_symmetrical(pattern):
        return 'vertically symmetric'
    else:
        return 'imperfect'

