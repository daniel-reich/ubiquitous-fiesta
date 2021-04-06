
def separate_numbers(s):
  for i in range(1,1+len(s)//2):
    cand = int(s[:i])
    test = str(cand)
    while len(test) < len(str(s)):
      cand += 1
      test += str(cand)
    if test == s:
      return 'YES ' + s[:i]
  
  return 'NO'

