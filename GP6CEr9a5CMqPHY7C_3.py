
def words_to_sentence(words):
  words = '' if not words else [i for i in words if i]
  if not words: return ''
  return ' and '.join([', '.join(words[:-1]), words[-1]]) if len(words) > 1 else words[0]

