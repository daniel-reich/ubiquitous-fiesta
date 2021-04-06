
def complete_square(arr):
    rows, cols = len(arr), len(arr[0])
    if rows == cols:
        return arr
    if rows > cols:
        return [x + [0]*(rows-cols) for x in arr]
    for i in range(cols-rows):
        arr.append([0]*cols)
    return arr

