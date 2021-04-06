
def sentence(words):
  v='aeiou'
  A=[]
  for x in words:
    if x[0] in v:
      A.append('an')
    else:
      A.append('a')
  B=[x[0]+' '+x[1] for x in zip(A, words)]
  if len(words)==2:
    return ' and '.join(B).capitalize()+'.'
  else:
    return (', '.join(B[:-1])+' and '+B[-1]).capitalize()+'.'

