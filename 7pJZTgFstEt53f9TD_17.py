
def transpose_matrix(lst):
    transposed_matrix = [[] for _ in range(len(lst[0]))]
    for col, row in enumerate(lst):
        for ind, element in enumerate(row):
            transposed_matrix[ind].append(element)
    return transposed_matrix

