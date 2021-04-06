
def text_to_number_binary(txt):
  dic = {"zero":"0", "one":"1"}
  b = ''.join(dic[w] for w in txt.lower().split() if w in dic)
  return b[:len(b)-len(b)%8]

