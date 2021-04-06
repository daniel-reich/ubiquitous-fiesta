
from string import ascii_lowercase as a
import re
def eadibitan(word):
  c = re.sub("[aeiouy]","",a)
  p = re.compile(r"([{0}y])([{0}y]|)([^{0}])([^{0}]|)([^{0}]|)([{0}](?=[{0}]|\b)|)".format(c))
  return p.sub(r"\2\3\1\4\5\6", word)

