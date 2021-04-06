
vowels = 'aeiou'
def same_vowel_group(w):
  vs = lambda x: set([a for a in x if a in vowels])  #vowels set
  cs = set(b for b in w[0] if b in vowels)  #comparison set
  return [word for word in w if vs(word) == cs]

