
def count_substring(s):
  count = 0
  for i, c in enumerate(s):
    if c == 'A':
      count += s.count('X', i+1)
  return count

