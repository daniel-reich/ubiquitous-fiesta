
def find_series(triplets, length, diff):
    for start in range(len(triplets) - length + 1):
        series = [start]
        value = triplets[start]
        cur = start + 1
        for k in range(length - 1):
            value += diff
            while cur < len(triplets) and triplets[cur] != value:
                cur += 1
            if cur == len(triplets):
                break
            series.append(cur)
        if len(series) == length:
            return series
    return []
​
def secret_word(string, length):
    triplet = ord(string[0]) - 96 + ord(string[1]) - 96 + ord(string[2]) - 96
    triplets = [triplet]
    for i in range(3, len(string)):
        triplet = triplet - (ord(string[i - 3]) - 96) + (ord(string[i]) - 96)
        triplets.append(triplet)
    for diff in range(1, 25):
        series = find_series(triplets, length, diff)
        if len(series) > 0:
            ans = ''.join([string[s+1] for s in series])
            return ans

