
def bell(layers):
    tri = [[1]]
    for i in range(1, layers):
        layer = [tri[i-1][-1]]
        for j in range(i):
            layer.append(tri[i-1][j] + layer[j])
        tri.append(layer)
    return tri[-1][-1]

