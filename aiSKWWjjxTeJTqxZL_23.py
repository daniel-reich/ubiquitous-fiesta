
def complete_square(arr):
    W, H = len(arr[0]), len(arr)
    if W == H:
        return arr
    if W < H:
        for r in range(H):
            arr[r] += [0] * (H - W)
    else:
        for i in range(W - H):
            arr.append([0] * W)
    return arr

