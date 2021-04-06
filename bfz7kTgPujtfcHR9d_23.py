
import re
def x_pronounce(sentence):
  return re.sub(r'x','cks',re.sub(r'(?<!\w)x','ecks',re.sub(r'(?<!\w)x(?=\w)','z',sentence)))

