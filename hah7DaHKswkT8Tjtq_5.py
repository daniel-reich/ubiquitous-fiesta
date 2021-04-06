
def separate_numbers(s):
  for i in range(1,len(s)//2+1):
    tmp,res = int(s[:i]),s[:i]
    while len(res) < len(s):
      tmp += 1
      res += str(tmp)
    if res == s:
      return 'YES '+s[:i]
  return 'NO'

