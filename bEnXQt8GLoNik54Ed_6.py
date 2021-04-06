
def max_score(s):
    if len(s) == 2:
        ans = 1 if s[0] == '0' else 0
        ans += 1 if s[1] == '1' else 0
        return ans
    ans = 0
    for i in range(1, len(s)):
        left, right = s[:i], s[i:]
        ans = max(ans, left.count('0') + right.count('1'))
    return ans

