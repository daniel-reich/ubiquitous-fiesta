
def maximum_seating(lst):
    ans = 0
    n = len(lst)
    for i in range(n):
        if lst[i] == 0 and 1 not in lst[max(0, i-2):min(n, i+3)]:
            ans += 1
            lst[i] = 1
    return ans

