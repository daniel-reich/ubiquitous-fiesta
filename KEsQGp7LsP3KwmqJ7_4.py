
def check(arr):
    min_val_idx = arr.index(min(arr))
    if min_val_idx == 0:
        return 'NO'
    return 'YES' if arr[min_val_idx:] + arr[:min_val_idx] == sorted(arr) else 'NO'

