
import re
def find_shortest_words(txt):
  txt = re.sub(r"[^a-zA-Z ]","",txt)
  mLen = min([len(word) for word in txt.split()])
  return sorted([word.lower() for word in txt.split() if len(word)==mLen])

