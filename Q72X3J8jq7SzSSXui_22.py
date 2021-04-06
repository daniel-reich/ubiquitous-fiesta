
import re
def sentence_searcher(txt, word):
  for sentence in re.split(r'(?<=\.) ', txt):
    if word.lower() in sentence.lower(): 
      return sentence
  return ""

