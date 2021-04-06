
import re
def no_yelling(phrase):
  if not phrase.endswith("?") and not phrase.endswith("!"): return phrase
  s = re.sub("\?{2,}$", "?", phrase)
  return re.sub("!{2,}$", "!", s)

