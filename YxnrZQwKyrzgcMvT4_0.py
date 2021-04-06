
def rotate_transform(arr, num):
    for _ in range(num % 4):
        arr = [list(col)[::-1] for col in zip(*arr)]
    return arr

