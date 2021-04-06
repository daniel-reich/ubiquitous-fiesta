
def same_vowel_group(w):
  return [i for i in w if set(j for j in i if j in 'aeiou') == set(j for j in w[0] if j in 'aeiou')]

