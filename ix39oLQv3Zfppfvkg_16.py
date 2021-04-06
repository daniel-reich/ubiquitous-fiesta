
def matrix_results(table1, table2):
    result = 0
    for f, b in zip(table1, table2):
        result = result + (f * b)
    return result;
​
def transpose_matrix(matrix):
    newMatrix = []
    for c in range(0, len(matrix[0])):
        newMatrix.append([])
    for m in matrix:
        loop = 0
        for p in m:
            newMatrix[loop].append(p)
            loop = loop + 1
    return newMatrix;
​
def multiply_matrix(matrix1, matrix2):
    matrix2 = transpose_matrix(matrix2)
    if len(matrix1) == len(matrix2):
        resultMatrix = []
        for n in range(0, len(matrix1)):
            temptemp = []
            for m in range(0, len(matrix2)):
                temptemp.append(matrix_results(matrix1[n], matrix2[m]))
            resultMatrix.append(temptemp)
        return resultMatrix;
    else:
        return "ERROR";

