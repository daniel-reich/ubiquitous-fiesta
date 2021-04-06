
from collections import Counter
def find_the_difference(s, t):
  if set(s)!=set(t):
    return list(set(t)-set(s))[-1]
  else:
    S, T=Counter(s), Counter(t)
    for x in S:
      if S[x]!=T[x]:
        return x

