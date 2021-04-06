
def encrypt(word):
  word = word[::-1]
  word = word.translate(str.maketrans('aeou','0123'))
  word += 'aca'
  return word

