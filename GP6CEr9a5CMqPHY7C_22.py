
def words_to_sentence(words):
  if words == None:
    return ""
  elif (len(words) == 0 or words[0] == ""):
    return ""
  elif len(words) == 1:
    return words[0]
  else:
    if "" in words:
      words.remove("")
    temp = ", ".join([words[i] for i in range(len(words)-1)])
    return temp + " and " + words[-1]

