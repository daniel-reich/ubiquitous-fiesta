
def can_put(txt, dim):
  words = txt.split(" ")
  numline = dim[0]
  linelen = dim[1]
  spaceleft = linelen
  linesleft = numline
  for word in words:
    wordlen = len(word)
    if wordlen > linelen:
      return False
    if (spaceleft < wordlen):
      linesleft -= 1
      spaceleft = linelen - (wordlen + 1)
      if linesleft == 0:
        return False
    else:
      spaceleft -= wordlen
      if spaceleft > 0:
        spaceleft -= 1
  return True

