
def diamond_sum(n):
    arr = []
    for i in range(1, 1 + n**2, n):
        arr.append(list(range(i, n+i)))
    mid = n // 2
    tot = get_sum(arr[:mid + 1])
    tot += get_sum(arr[mid + 1:][::-1])
    return tot
​
def get_sum(a):
    if not a: return 0
    mid = len(a[0]) // 2
    tot = a[0][mid]
    di = 1
    for r in range(1, len(a)):
        tot += a[r][mid-di] + a[r][mid+di]
        di += 1
    return tot

