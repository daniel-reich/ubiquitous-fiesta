
def cleave(string, lst):
  if not string:
    return ''
  for word in lst:
    if string.startswith(word):
      r = cleave(string[len(word):],lst)
      if r == "Cleaving stalled: Word not found":
        continue
      return word + ' ' + r if r else word
  return "Cleaving stalled: Word not found"

