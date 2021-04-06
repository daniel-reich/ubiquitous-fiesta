
def handle_comma(words):
    s = ""
    for i in range(0, len(words)):
      if i == len(words) - 1:
        s = s[:-2]
        s += " and " + words[i]
      else:
        s += words[i] + ", "
    return s
    
def words_to_sentence(words):
  if words == None:
    return ""
  words = [i for i in words if i != ""]
  if len(words) == 0:
    return ""
  elif len(words) == 2:
    return words[0] + " and " + words[1]
  elif len(words) > 2:
    return handle_comma(words)
  else:
    return words[0]

