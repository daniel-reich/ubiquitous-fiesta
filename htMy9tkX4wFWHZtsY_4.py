
def palindrome_time(lst):
  h1 = lst[0]
  m1 = lst[1]
  s1 = lst[2]
  h2 = lst[3]
  m2 = lst[4]
  s2 = lst[5]
  count = 0
  keepGoing = True
  while (keepGoing): 
    if ((h1 % 10) == (s1 // 10) and (s1 % 10) == (h1 // 10) and (m1 % 11) == 0):
      count = count + 1
    if h1 == h2 and m1 == m2 and s1 == s2:
      keepGoing = False
    s1 = s1 + 1
    if (s1 == 60):
      s1 = 0
      m1 = m1 + 1
      if (m1 == 60):
        m1 = 0
        h1 = h1 + 1
  return count

