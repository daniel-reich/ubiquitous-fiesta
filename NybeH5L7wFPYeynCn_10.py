
def three_letter_collection(s):
  l = []
  n = 0
  while(n<len(s)-2):
    l.append(s[n:n+3])
    n += 1
  return sorted(l)

