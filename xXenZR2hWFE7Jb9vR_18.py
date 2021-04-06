
def is_isomorphic(s, t):
  d1=dict([(s[i],t[i]) for i in range(len(s))])
  d2=dict([(t[i],s[i]) for i in range(len(t))])
  return all([d1[s[i]]==t[i] for i in range(len(s))]) and all([d2[t[i]]==s[i] for i in range(len(t))])

