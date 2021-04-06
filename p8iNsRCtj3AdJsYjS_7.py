
def title_to_number(s):
  a = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  s = s[::-1]
  ret = 0
  for i in range(len(s)):
    ret+=a.index(s[i])*(26**i)
  return ret

