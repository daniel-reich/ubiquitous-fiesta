
def camelCasing(txt):
  new_txt = txt.replace("_", " ").split()
  new_sentence_lst = []
  count = 0
  for word in new_txt:
    if count == 0:
      new_sentence_lst.append(word.lower())
    else:
      new_sentence_lst.append(word.capitalize())
    count += 1
  return "".join(new_sentence_lst)

