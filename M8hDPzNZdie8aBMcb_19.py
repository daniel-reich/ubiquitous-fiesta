
def count_substring(s):
  ass = []
  xs = []
  count = 0
  for i in range(len(s)):
      if s[i] == 'A':
          ass.append(i)
      if s[i] == 'X':
          xs.append(i)
  for x in ass:
      for y in xs:
          if x < y:
              count += 1
  return count

