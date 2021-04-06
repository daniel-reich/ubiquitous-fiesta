
def conjugate(verb, pronoun):
  pronouns = [['Io','o'], ['Tu','i'], ['Egli','a'], ['Noi','iamo'], 
        ['Voi','ate'], ['Essi','ano']]
  verb, pn = verb[:-3], pronouns[pronoun-1] 
  if verb[-1] in 'cg':
    verb += 'h'
  if verb[-1] == 'i':
    pn[1] = pn[1].replace('i','')
  return '{} {}'.format(pn[0], verb + pn[1])

