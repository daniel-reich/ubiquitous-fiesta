
def replace_vowel(word):
  trans = {'a':"1",'e':"2",'i':"3",'o':"4",'u':"5"}
  return ''.join(trans[ch] if ch in trans else ch for ch in word)

