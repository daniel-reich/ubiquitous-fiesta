
def conjugate(verb, pron):
  verb = verb.rstrip('are')
  conj = {1:('Io','o'), 2:('Tu','i'), 3:('Egli','a'), 
  4:('Noi','iamo'), 5:('Voi','ate'), 6:('Essi','ano')}
  if (verb.endswith('c') or verb.endswith('g')) and (pron == 2 or pron == 4):
    return conj[pron][0] + ' ' + verb + 'h' + conj[pron][1]
  elif verb.endswith('i') and (pron == 2 or pron == 4):
    return conj[pron][0] + ' ' + verb.rstrip('i') + conj[pron][1]
  else:
    return conj[pron][0] + ' ' + verb + conj[pron][1]

