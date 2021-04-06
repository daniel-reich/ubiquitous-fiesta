
def min_swaps(string):
    return min(swap(string, '0'), swap(string, '1'))
​
def swap(s, prev):
    cnt = 0
    for x in s:
        if x == prev:
            cnt += 1
        prev = str(1-int(prev))
    return cnt

