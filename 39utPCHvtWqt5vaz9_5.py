
def direction(lst):
  a = '  '.join(i for i in lst)
  b = a.maketrans('eastEAST','westWEST')
  return a.translate(b).split('  ')

