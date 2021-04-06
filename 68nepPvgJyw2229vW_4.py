
def pairwise_swap(A):
    n = len(A)
    for k in range(n // 2):
        A[2*k:2*k+2] = A[2*k:2*k+2][::-1]
    if n % 2 == 0:
        return A
    asc = [sum([ord(c) for c in str(a)]) for a in A]
    high = 0
    idx = 0
    for i in range(n):
        if asc[i] > high:
            high = asc[i]
            idx = i
    if idx == n - 1:
        return A
    A[idx], A[-1] = A[-1], A[idx]
    return A

