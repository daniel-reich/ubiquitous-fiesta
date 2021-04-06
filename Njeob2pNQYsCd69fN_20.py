
import re
​
def prevent_distractions(txt):
  bad_words = [
  "anime",
  "meme",
  "vine",
  "roasts",
  "Danny DeVito"
  ]
  for w in bad_words:
    if re.search(w, txt):
      return 'NO!'
  return 'Safe watching!'

