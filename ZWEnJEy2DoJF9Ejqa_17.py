
def edabit_in_string(txt):
  i = 0
  for c in txt:
    if c == 'edabit'[i]:
      if i == 5:
        return "YES"
      i += 1
  return "NO"

