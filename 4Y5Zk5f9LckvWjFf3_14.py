
def special_reverse(s, c):
  wordlist = s.split(' ')
  newwords = []
  for word in wordlist:
    if word[0] != c:
      newwords.append(word)
    else:
      newwords.append(word[::-1])
  return (' ').join(newwords)

