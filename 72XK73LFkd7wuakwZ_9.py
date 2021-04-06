
def junction_or_self(n):
  jun = []
  for i in range(n):
    s = str(i)
    sum = 0
    for j in range(len(s)):
      d = int(s[j])
      sum += d
    if sum + i == n:
      jun.append(i)
  
  
  if len(jun) == 0:
    return "Self"
  else:
    jun.reverse()
    return jun

