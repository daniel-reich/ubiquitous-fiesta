
def inatorInator(word):
  if word.lower()[-1] not in 'aieou':
    return '{}inator {}000'.format(word,len(word))
  else:
    return '{}-inator {}000'.format(word,len(word))

