
points = [2, 3, 6, 7, 8]
lookup = {}
def football(score, n=4):
    if score == 0: return 1
    if score < 0 or n < 0: return 0
    key = (n, score)
    if key in lookup:
        res = lookup[key]
    else:
        res = football(score-points[n], n) + football(score, n-1)
        lookup[key] = res
    return res

