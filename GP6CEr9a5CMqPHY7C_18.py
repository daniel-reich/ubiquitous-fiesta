
def words_to_sentence(words):
  if not words or not words[0]: return ''
  if len(words) == 1: return words[0]
  
  words = [x for x in words if x]
  words[-1] = 'and ' + words[-1]
  words = [x + ',' for x in words[:-2]] + words[-2:]
  return ' '.join(words)

