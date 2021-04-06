
# with Bonus (no permutations)
def next_number(n):
    s = [int(i) for i in str(n)]
​
    for i in range(len(s)-1, 0, -1):
        if s[i-1] < s[i]:
            digit = s[i-1]
            while digit not in s[i:]:
                digit += 1
            nearest = s[i:].index(digit) + i
            s[i-1], s[nearest] = s[nearest], s[i-1]
            s[i:] = sorted(s[i:])
            return int(''.join(str(i) for i in s))
    return n

