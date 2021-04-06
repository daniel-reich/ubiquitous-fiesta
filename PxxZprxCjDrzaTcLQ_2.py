
def vowel_links(txt):
  l, v = txt.split(), 'aeuio'
  return any(l[i][-1] in v and l[i+1][0] in v for i in range(len(l)-1))

