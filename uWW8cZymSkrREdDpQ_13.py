
def sums_up(v):
  s, pair = v[::-1], lambda e, r: sorted([e,
     r[r.index(8-e)]]) if 8-e in r else None
  return {"pairs": [pair(k, s[i+1:]) for i, k
     in enumerate(s) if pair(k, s[i+1:])][::-1]}

