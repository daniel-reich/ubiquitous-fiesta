
def ascending(txt):
    for i in range(1, len(txt) + 1):
        arr = [int(txt[s:s + i]) for s in range(0, len(txt), i)]
        if len(arr) > 1 and all([1 if arr[j] == arr[j - 1] + 1 else 0 for j in range(1, len(arr))]):
            return 1
    return 0

