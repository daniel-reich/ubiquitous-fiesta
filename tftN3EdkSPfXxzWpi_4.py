
def sentence_searcher(txt, n):
  n = (len(txt.split()) + n)%len(txt.split())
  sentences = []
  count = 0
  for i in txt.split("."):
    i = i.strip()
    i += "."
    sentences.append(i.split())
  for i in sentences:
    if count <= n and n < count + len(i):
      return " ".join(i)
    else:
      count += len(i)

