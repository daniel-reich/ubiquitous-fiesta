
def title_to_number(s):
  alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  n = 0
  for i in range(len(s)):
    n+=alphabet.find(s[-i-1])*(26**i)
  return n

