
def square_root(n):
    low, high = 1, n
    while low <= high:
        mid = (low + high) // 2
        sq = mid**2
        if sq == n:
            return mid
        if sq < n:
            low = mid + 1
            ans = mid
        else:
            high = mid - 1
    return ans

