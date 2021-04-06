
def alphabet_index(txt):
  return " ".join([str(ord(i.lower()) - 96) for i in txt if i.isalpha()])

