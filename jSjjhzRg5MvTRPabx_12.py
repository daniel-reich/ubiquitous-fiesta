
def sentence(words):
  for i in range(1,len(words)):
    words[i] = ['a ','an '][words[i][0] in 'aeiou'] + words[i]
  words = ', '.join(words[:-1]) + ' and ' + words[-1] + '.'
  return ['A ','An '][words[0] in 'aeiou']+words

