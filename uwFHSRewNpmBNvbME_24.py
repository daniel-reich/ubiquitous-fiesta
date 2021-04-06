
def same_vowel_group(w):
  a=set(i for i in w[0] if i in 'aeiou')
  return [i for i in w if set(x for x in i if x in 'aeiou')==a]

