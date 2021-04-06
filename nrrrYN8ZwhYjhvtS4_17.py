
def extend_vowels(word, n):
  if not isinstance(n, int) or n < 0:
    return 'invalid'
  return ''.join(ch+ch*n if ch.lower() in 'aeiou' else ch for ch in word)

