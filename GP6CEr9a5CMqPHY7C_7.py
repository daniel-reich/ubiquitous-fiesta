
def words_to_sentence(words):
  a = ""
  i = 0
  c = []
  if words == None or len(words) == 0:
    return ""
  elif len(words) == 1:
    return words[0]
  for index in words:
    if index != "":
      c.append(index)
  while i < len(c)-1:
    a += c[i]
    if i == len(c) -2 : 
      break
    a += ", "
    i += 1
  a = a + " and " + c[i+1]  
  return a

