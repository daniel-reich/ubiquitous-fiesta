
def subtract_matrix(lst1, lst2):
    return [[float(lst1[row][col]) - float(lst2[row][col]) for col in range(len(lst1[0]))] for row in range(len(lst1))]

