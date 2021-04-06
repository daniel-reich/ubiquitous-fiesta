
def vowel_links(txt):
  return any(x[-1] in "aeiou" and y[0] in "aeiou" for x,y in zip(txt.split(),txt.split()[1:]))

