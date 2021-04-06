
def words_to_sentence(words):
  if not words:
    return ""
  words = [i for i in words if i]
  if len(words) > 2:
    return ', '.join(words[:-1])+' and '+words[-1]
  return ' and '.join(words)

