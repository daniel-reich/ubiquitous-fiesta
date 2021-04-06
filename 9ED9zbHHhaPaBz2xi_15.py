
seq = [1, 2, 0, 2, 2, 1, 0, 1]
def normal_sequence(n):
    return seq[(n - 3) % 8] if n > 2 else n - 1

