
import codecs
def first_index(hex_txt, needle):
  n = codecs.encode(needle.encode(encoding="utf-8"), 'hex')
  for ind,i in enumerate(hex_txt.split()):
    if i == str(n)[2:4]:
      return ind

