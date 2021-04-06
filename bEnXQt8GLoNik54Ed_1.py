
def max_score(s):
    max = 0
    for i in range(len(s)-1):
        left = s[0:i+1]
        right = s[i+1:]
        score = left.count('0') + right.count('1')
        max = score if score > max else max
    return max

