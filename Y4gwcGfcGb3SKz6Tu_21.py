
def max_separator(txt):
  sub = []
​
  for i in range(len(txt)-1):
    for j in range(i+1, len(txt)):
      if txt[i] == txt[j] and txt[i:j+1].count(txt[i]) == 2:
        sub.append(txt[i:j+1])
​
  longest = max(map(len, sub), default=0)
  return sorted(s[0] for s in sub if len(s) == longest)

