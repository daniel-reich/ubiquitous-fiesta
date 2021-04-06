
def sentence(words):
  end=" and an "+words[-1] if words[-1][0] in "aeiou" else " and a "+words[-1]
  return ", ".join("an "+word if word[0] in "aeiou" else "a "+word for word in words[:-1]).capitalize()+end+"."

