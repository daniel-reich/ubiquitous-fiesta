
def no_yelling(phrase):
  words = phrase.split()
  last = words[-1]
  if "!" not in last and "?" not in last:
    return phrase
  mark = "!" if last.find("!")>last.find("?") else "?"
  pos = last.find(mark)
  res = " ".join(words[i] for i in range(len(words)-1))
  if len(words)>1: res += " "
  res += last[0:pos] + mark
  return res

