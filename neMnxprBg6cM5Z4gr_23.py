
def arithmetic_progression(start, diff, n):
  l=[start]
  while len(l)<n:
    l.append(l[-1]+diff)
  return ", ".join(map(str,l))

