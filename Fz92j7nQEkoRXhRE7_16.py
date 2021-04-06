
def jumping_frog(n, stones):
    min_s = [len(stones) + 2] * len(stones)
    for j in range(len(stones)):
        for i in range(len(stones) - 1, -1, -1):
            forward = i + stones[i]
            backward = i - stones[i]
            right = 1 if forward >= len(stones) else min_s[forward]
            left = min_s[backward] if backward >= 0 else len(stones) + 2
            min_s[i] = 1 + min(right, left)
    if min_s[len(stones) - n] >= len(stones) + 2:
        return 'no chance :-('
    return min_s[len(stones) - n]

