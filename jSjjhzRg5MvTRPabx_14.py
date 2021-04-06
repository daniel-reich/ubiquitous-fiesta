
def sentence(words):
  v = ['a', 'e', 'i', 'o', 'u']
  return ', '.join('a '+w if w[0] not in v else 'an '+w for w in words[:-1]).capitalize() + ' '.join(' and a '+w+'.' if w[0] not in v else ' and an '+w+'.' for w in words[-1:])

