
def blah_blah(txt, n):
  s = txt.split()
  return " ".join('blah' if idx >= len(s)-n else word for idx,word in enumerate(s)) + "..."

