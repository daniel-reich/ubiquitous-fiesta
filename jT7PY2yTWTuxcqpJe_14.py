
def spiral_order(matrix):
    a = []
​
    while matrix:
        a.append(list(matrix[0]))
        matrix = list(zip(*matrix[1:]))[::-1]
    
    return sum(a, [])

