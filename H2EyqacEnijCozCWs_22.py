
def first_n_vowels(txt, n):
  vowels = ''.join([i for i in txt if i in 'aeiou'])
  return vowels[:n] if len(vowels) >= n else 'invalid'

