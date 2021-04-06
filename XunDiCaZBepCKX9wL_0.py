
def secret_word(s, l):
    vals = [sum(ord(c) for c in s[i-1:i+2]) for i in range(1, len(s)-1)]
    for i, v in enumerate(vals):
        for w in vals[i+1:]:
            cat = subseq(vals, [v+(w-v)*k for k in range(l)])
            if cat is not None:
                return ''.join(s[c+1] for c in cat)
​
def subseq(s1, s2):
    if not s2:
        return []
    if s2[0] in s1:
        i = s1.index(s2[0])
        meh = subseq(s1[i+1:], s2[1:])
        if meh is not None:
            return [i] + [m+i+1 for m in meh]

