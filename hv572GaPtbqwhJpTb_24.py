
def elasticize(word):
    ln = len(word)
    if ln < 3:
        return word
    mid = ln // 2
    if ln % 2 == 0:
        left = word[:mid]
        right = word[mid:]
        pivot = ''
    else:
        left = word[:mid]
        right = word[mid+1:]
        pivot = word[mid]
    left = expand(left)
    right = expand(right[::-1])[::-1]
    return left + (mid+1)*pivot + right
​
def expand(word):
    ans = ''
    for idx, w in enumerate(word, start=1):
        ans += idx*w
    return ans

