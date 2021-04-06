
def max_score(s):
    max_score = max(s[:-1].count("0") + s[-1].count("1"), s[0].count("0") + s[1:].count("1"))
    for i in range(1, len(s) - 1):
        cnt = s[:i].count("0") + s[i:].count("1")
        max_score = max(max_score, cnt)
    return max_score

