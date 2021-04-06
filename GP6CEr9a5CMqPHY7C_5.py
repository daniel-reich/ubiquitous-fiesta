
def words_to_sentence(words):
  if words == None:
    return ""
  words = [i for i in words if i]
  return ", ".join(words[:-1]) + " and " + words[-1] if len(words) > 2 else words[0] + " and " + words[1] if len(words) == 2 else words[0] if words else ""

