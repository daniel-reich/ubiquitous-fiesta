
def conjugate(verb, pronoun):
  pro = {1:['Io','o'],
2:['Tu','i'],
3:['Egli','a'],
4:['Noi','iamo'],
5:['Voi','ate'],
6:['Essi','ano']}
  pn = pro[pronoun]
  root = verb[:-3]
  if root[-1] in 'cg' and pronoun in [2,4]:
    return '{} {}{}'.format(pn[0],root,'h'+pn[1])
  elif root[-1]=='i' and pronoun in [2,4]:
    return '{} {}{}'.format(pn[0],root[:-1],pn[1])
  return '{} {}{}'.format(pn[0],root,pn[1])

