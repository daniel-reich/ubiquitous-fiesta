
def longest_word(s):
  s = s.split()
  x = ""
  for i in s:
    if len(i)>len(x):
      x=i
  return x

