
def count_substring(txt):
  total = 0
  for i in range(len(txt)):
    if txt[i] == 'A':
      total += txt[i:].count('X')
  return total

