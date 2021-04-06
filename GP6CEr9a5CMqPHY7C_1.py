
def words_to_sentence(words):
  if not words:
    return ""
  if len(words) == 1:
    return words[0]
  words = [w for w in words if w]
  return ", ".join(words[:-1]) + " and " + words[-1]

