
def extend_vowels(word, num):
  return ''.join([c*num+c if c in 'aeiouAEIOU' else c for c in word]) if type(num)==int and num>=0 else 'invalid'

