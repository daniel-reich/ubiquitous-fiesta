
def vowel_links(txt):
  v = 'aeiou'
  lst = txt.split()
  return any(a[-1] in v and b[0] in v for a,b in zip(lst, lst[1:]))

