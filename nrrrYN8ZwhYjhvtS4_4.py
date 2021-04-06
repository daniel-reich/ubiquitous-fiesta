
def extend_vowels(word, num):
  return ''.join((x*num)+x if x in 'aeiouAEIOU' else x for x in word) if num>=0 and int(num)==num else 'invalid'

