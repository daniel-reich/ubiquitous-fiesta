
def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
​
def max_sum_pair(lst):
    M = max_subarray(lst)
    for k in range(1, len(lst) - 1):
        m1, m2 = max_subarray(lst[:k]), max_subarray(lst[k:])
        M = max(M, m1 + m2)
    return M

