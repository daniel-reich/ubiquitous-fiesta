
def sentence_searcher(txt, word):
  split_text = txt.split(".")
  for i in split_text:
    if word.lower() in i.lower():
      return i.strip() + "."
  return ""

