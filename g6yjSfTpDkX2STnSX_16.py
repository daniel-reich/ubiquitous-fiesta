
def convert_to_hex(txt):
  import re,codecs
  return " ".join(re.findall(r'\w\w',str(codecs.encode(txt.encode(), "hex")).replace("'","")[1:]))

