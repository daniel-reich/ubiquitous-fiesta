
def fix_import(s):
  words = s.split(" ")
  words[0], words[2] = words[2], words[0]
  words[1], words[3] = words[3], words[1]
  return " ".join(words)

