
import re
def is_parsel_tongue(sentence):
  def isss(word):
    if 's' in word.lower() and not re.search(r's{2,}', word.lower()):
      print(word)
      return False
    return True
  return all([isss(word) for word in sentence.split()])

