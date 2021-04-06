
def extend_vowels(word, num):
  if num<0 or num%1: return 'invalid'
  return ''.join(ch*(num+1) if ch.lower() in 'aeiou' else ch for ch in word)

