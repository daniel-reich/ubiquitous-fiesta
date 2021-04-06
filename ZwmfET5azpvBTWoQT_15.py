
import re
def valid_word_nest(word, nest):
  while len(nest)>len(word):
    if bool(re.search(word, nest)):
      if len(re.findall(word, nest))>1:
        return False
      else:
        nest=re.sub(word, '', nest)
    else:
      return False
  return word==nest

