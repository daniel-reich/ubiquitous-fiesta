
def words_to_sentence(words):
  if not words or words is None:
    return ""
  elif len(words) == 1:
    return words[0]
  else: 
    words = list(filter(lambda x: x != "",words))
    sentence = ''.join(list(map(lambda x: x + ", ",words[:-1])))
    return sentence[:-2] + " and " + words[-1]

