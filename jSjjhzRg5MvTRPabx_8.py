
def sentence(words):
  if words[0][0] in 'aeiou':
    ret = 'An '+words[0]
  else:
    ret = 'A '+words[0]
  for i in range(1,len(words)-1):
    if words[i][0] in 'aeiou':
      ret+=', an '+words[i]
    else:
      ret+=', a '+words[i]
  if words[-1][0] in 'aeiou':
    ret+=' and an '+words[-1]+'.'
  else:
    ret+=' and a '+words[-1]+'.'
  return ret

