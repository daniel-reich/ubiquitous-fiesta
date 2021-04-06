
def max_score(s):
  total = (1 if s[0] == "0" else 0) + sum(s[i] == "1" for i in range(1, len(s)))
  max_total = total
  for i in range(1, len(s)-1):
    total += 1 if s[i] == "0" else -1
    if total > max_total:
      max_total = total
  return max_total

