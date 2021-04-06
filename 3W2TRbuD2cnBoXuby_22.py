
def collect(s, n):
    slices = []
    if len(s) < n:
        return []
    for i in range(len(s)):
        if i % n == 0:
            slices.append(s[i:i+n])
    slices = sorted(slices)
    new_slices = []
    for i in range(len(slices)):
        if len(slices[i]) == n:
            new_slices.append(slices[i])
​
    return new_slices

