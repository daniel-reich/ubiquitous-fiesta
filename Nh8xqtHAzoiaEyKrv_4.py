
def correct_sentences(s):
  a = " ".join(s.split())
  b = "".join(["*" + i if i.isupper() else i for i in a]).split("*")
  return " ".join([i.capitalize().strip()+"." for i in b])

