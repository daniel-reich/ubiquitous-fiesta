
import re
def sentence_searcher(txt, word):
  x = re.search(r"[\. ]*([a-z ]*{}[a-z ]*\.)".format(word), txt, re.I)
  return x.group(1) if x else ''

