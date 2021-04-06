
import re
def constraint(txt):
  if all(txt.lower().count(l) for l in "qwertyuiopasdfghjklzxcvbnm"):
    return "Pangram"
  if all(txt.lower().count(l)<2 for l in "qwertyuiopasdfghjklzxcvbnm"):
    return "Heterogram"
  words = re.findall(r"\b\w+\b",txt.lower())
  if len(set(w[0] for w in words)) == 1:
    return "Tautogram"
  if any(all(l in w for w in words) for l in "qwertyuiopasdfghjklzxcvbnm"):
    return "Transgram"
  return "Sentence"

