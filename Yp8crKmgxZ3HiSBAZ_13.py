
def dfs(lst, el, freq, level):
    if level not in freq:
        freq[level] = 0
    for k in lst:
        if type(k) == int:
            if k == el:
                freq[level] = freq.get(level, 0) + 1
        else:
            freq = dfs(k, el, freq, level + 1)
    return freq
​
def freq_count(lst, el):
    freq = dfs(lst, el, {}, 0)
    ans = [[k, freq.get(k, 0)] for k in range(max(freq.keys()) + 1)]
    return ans

