
import re
def scrambled(words, mask):
  return re.compile(r"\b{}\b".format(mask.replace("*", "\w"))).findall(" ".join(words))

