
def combine(lst):
    ans = {}
    for s_start, b, s_end in lst:
        if s_start not in ans:
            ans[s_start] = ['_', '_']
        ans[s_start][b] = s_end
    return ans

