
def sle(nested_list):
    A = [nested_list[0][:2], nested_list[1][:2]]
    b = [nested_list[0][2], nested_list[1][2]]
    x = [0, 0]
    def det(matrix):
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    if det(A) == 0:
        return False
    else:
        x[0] = int((b[0] * A[1][1] - A[0][1] * b[1]) / (A[0][0] * A[1][1] - A[0][1] * A[1][0]))
        x[1] = int((b[1] * A[0][0] - A[1][0] * b[0]) / (A[0][0] * A[1][1] - A[1][0] * A[0][1]))
        return tuple(x)

