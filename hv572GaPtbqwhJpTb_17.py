
def rifa(ans, n, c):
    ans += n * c
    return ans
​
def elasticize(word):
    m = len(word) // 2
    p = m
    ans1 = ans2 = ''
    for i in range(m):
        ans1 = rifa(ans1, i+1, word[i])
    if len(word) % 2:
        ans1 += word[m:m+1] * (m+1)
        m += 1
    for i in range(m, len(word)):
        ans2 = rifa(ans2, p, word[i])
        p -= 1
    return ans1 + ans2

