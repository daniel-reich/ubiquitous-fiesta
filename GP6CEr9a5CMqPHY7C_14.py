
def words_to_sentence(words):
  if words == None or len(words) == 0:
    return ''
  words = [x for x in words if x not in ', ']
  if len(words) < 2:
    return ''.join(words)
  return ', '.join([x for x in words[:-1]]) + ' and ' + words [-1]

