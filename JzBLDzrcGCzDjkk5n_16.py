
def encrypt(word):
  word_rev = word[len(word)::-1]
  word_rev = word_rev.replace('a', '0')
  word_rev = word_rev.replace('e', '1')
  word_rev = word_rev.replace('o', '2')
  word_rev = word_rev.replace('u', '3')
  word_rev += "aca"
  return word_rev

