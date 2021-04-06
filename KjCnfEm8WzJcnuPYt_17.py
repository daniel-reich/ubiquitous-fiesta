
def zero_indices(lst, k):
    if k >= lst.count(0):
        return [k for k in range(len(lst)) if lst[k] == 0]
    left, count, window, leftIndex = 0, 0, 0, 0
    for right in range(len(lst)):
        if lst[right] == 0:
            count += 1
        while count > k:
            if lst[left] == 0:
                count -= 1
            left += 1
        if right - left + 1 > window:
            window = right - left + 1
            leftIndex = left
    return [k for k in range(leftIndex, min(leftIndex + window, len(lst))) if lst[k] == 0]

