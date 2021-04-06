
def retrieve(txt):
  if txt:
    return [i.lower().strip(".") for i in txt.split(" ") if i[0].lower() in "aeiou"]
  return []

