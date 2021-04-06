
seg_digits = {'0': 'abcdef', '1': 'bc', '2': 'abged', '3': 'abcdg',
              '4': 'fgcb', '5': 'afgcd', '6': 'afgcde',
              '7': 'abc', '8': 'abcdefg', '9': 'abcfg'}
​
def digit_change(d1, d2):
    if d1 == d2:
        return []
    change = []
    segs1 = seg_digits[d1]
    segs2 = seg_digits[d2]
    for seg1 in segs1:
        if seg1 not in segs2:
            change.append(seg1)
    for seg2 in segs2:
        if seg2 not in segs1:
            change.append(seg2.upper())
    return sorted(change, key=lambda x: x.lower())
​
def seven_segment(txt):
    ans = []
    for i in range(1, len(txt)):
        ans.append(digit_change(txt[i-1], txt[i]))
    return ans

