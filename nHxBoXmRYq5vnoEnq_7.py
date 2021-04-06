
def vowels(string, c=0):
  if not string: return c
  if string[0] in 'aeiou': c += 1
  return vowels(string[1:], c)

