
def camel_to_snake(s):
  def convert(word):
    caps = 'abcdefghijklmnopqrstuvwxyz'.upper()
    new_word = ''
    for l8r in word:
      if l8r in caps:
        new_word += '_' + l8r.lower()
      else:
        new_word += l8r
    return new_word
  
  words = s.split()
  
  return ' '.join(convert(word) for word in words)

