
def is_alphabetically_sorted(sentence):
  a = sentence.replace(".", "")
  b = a.replace(",", "")
  c = b.split(" ")
  for i in c:
    if len(i) >= 3:
      if "".join(sorted(list(i))) == i:
        return True
  return False

