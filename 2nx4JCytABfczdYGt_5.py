
def conjugate(verb, pr):
  l = [('Io', 'o'),('Tu','i'),('Egli','a'),
      ('Noi', 'iamo'), ('Voi', 'ate'), ('Essi', 'ano')]
  v = verb.replace('are','')
  if v[-1] in 'cg' and pr in[2,4]: v+='h'
  if v[-1] == 'i' and pr in[2,4]: v= v[:-1]
  return l[pr-1][0] + ' ' + v + l[pr-1][1]

