
def meme_sum(a, b):
    if max(a, b) == 0:
        return 0
    ans = ""
    while max(a, b) > 0:
        ans = str(a % 10 + b % 10) + ans
        a //= 10
        b //= 10
    return int(ans)

