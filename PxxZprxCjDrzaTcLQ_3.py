
def vowel_links(txt):
  words, v= txt.split(), 'aeiou'
  return any(words[i][-1] in v and words[i+1][0] in v for i in range(len(words)-1))

