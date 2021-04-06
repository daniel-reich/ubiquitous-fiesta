
def chunk(array, size):
    rows, rem = divmod(len(array), size)
    return [array[r * size: (r + 1) * size] for r in range(rows + bool(rem))]

