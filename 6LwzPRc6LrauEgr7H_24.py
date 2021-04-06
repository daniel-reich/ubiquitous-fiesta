
def worm_length(worm):
  if worm=='':
    return 'invalid'
  for i in worm:
    if i!='-':
      return 'invalid'
  else:
    return str(len(worm)*10)+' mm.'

