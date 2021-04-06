
def words_to_sentence(words):
  if not words: return ""
  w = [i for i in words if i]
  return "".join(w) if len(w)<2 else ", ".join(w[:-1]) + " and " + w[-1]

