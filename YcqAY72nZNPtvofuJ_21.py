
def quad_sequence(x):
    a = 0.5 * x[0] - x[1] + 0.5 * x[2]
    b = -2.5 * x[0] + 4 * x[1] - 1.5 * x[2]
    c = 3 * x[0] - 3 * x[1] + x[2]
    return [int(a * i * i + b * i + c)
            for i in range(len(x) + 1, 2 * len(x) + 1)]

