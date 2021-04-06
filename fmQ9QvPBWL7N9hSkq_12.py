
def unstretch(word):
  res_str = ""
  for i in range(len(word)):
    if i != (len(word) - 1):
      if word[i] != word[i+1]:
        res_str += word[i]
    else:
      if word[i] != res_str[-1]:
        res_str += word[i]
  return res_str

