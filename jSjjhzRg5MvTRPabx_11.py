
def sentence(words):
  a = ['an ' + a if a[0] in 'aeiou' else 'a ' + a for a in words]
  return ', '.join(a[0:-1]).capitalize() + ' and ' + a[-1] + '.'

