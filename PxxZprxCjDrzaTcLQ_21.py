
def vowel_links(txt):
  t=txt.split()
  v="aeiou"
  for i,w in enumerate(t[:-1]):
    if w[-1] in v and t[i+1][0] in v:
      return True
  return False

