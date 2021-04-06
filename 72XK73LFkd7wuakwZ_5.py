
def junction_or_self(n):
    ans = [i for i in range(1, n) if (i + sum([int(j) for j in str(i)]) == n)]
    if len(ans) > 0:
        ans.sort(reverse=True)
        return ans
    return "Self"

