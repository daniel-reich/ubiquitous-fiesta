
def censor_string(txt, lst, char):
  word_list=txt.split(" ")
  for word in word_list:
    if word in lst:
      replace_index=word_list.index(word)
      word_list[replace_index]=char*len(word)
  return " ".join(word_list)

