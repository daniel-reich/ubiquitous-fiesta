
def happiness_number(s):
  total = 0
  d = len(s)
  for i in range(d):
      if ':)' in s[i:i+2]:
          total += 1
      elif ':(' in s[i:i+2]:
          total -= 1
      elif '):' in s[i:i+2]:
          total -= 1
      elif '(:' in s[i:i+2]:
          total += 1
  return total

