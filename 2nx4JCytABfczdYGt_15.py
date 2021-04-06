
pronouns = ['Io ','Tu ','Egli ','Noi ','Voi ','Essi ']
suffix = ['o','i','a','iamo','ate','ano']
def conjugate(verb, pronoun):
  root = verb[:-3]
  if root[-1] in 'cg':
    return pronouns[pronoun-1]+root+'h'+suffix[pronoun-1]
  if root[-1] == 'i':
    return pronouns[pronoun-1]+root+''.join(x for x in suffix[pronoun-1] if x != 'i')
  return pronouns[pronoun-1]+root+suffix[pronoun-1]

