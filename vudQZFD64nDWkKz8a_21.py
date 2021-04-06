
def grant_the_hint(txt):
    low = txt.split()
    lou = ['_'*len(w) for w in low]
    ans = [' '.join(lou)]
    idx = len(max(low, key=len))
​
    for i in range(idx):
        nxt = []
        for j, w in enumerate(lou):
            if '_' in w:
                nxt.append(w[:i] + low[j][i] + w[i+1:])
            else:
                nxt.append(low[j])
        lou = nxt
        ans.append(' '.join(lou))
    return ans

