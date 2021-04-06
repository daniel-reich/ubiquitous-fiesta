
def vowel_links(txt):
  v = ['a', 'e', 'i', 'o', 'u']
  l = [word for word in txt.split(' ')] + [' ']
  vlink = lambda x: l[l.index(x)][-1] in v and l[l.index(x)+1][0] in v
  return any(vlink(w) for w in l)

