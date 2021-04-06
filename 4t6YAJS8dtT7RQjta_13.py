
def num_layers(n, i=0.0005):
    for _ in range(n):
        i *= 2
    return '{}m'.format(i)

