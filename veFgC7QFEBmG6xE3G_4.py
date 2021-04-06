
import re
def is_smooth(sentence):
  return all(i == i[::-1] for i in re.findall('. .',sentence.lower()))

