
def words_to_sentence(words):
  if words == None: return ""
  if "" in words: words.remove("")
  if len(words) == 1: return ''.join(words)
  return ("" if len(words) < 1 else str(', '.join(words[:-1]) + ' and ' + words[-1]))

