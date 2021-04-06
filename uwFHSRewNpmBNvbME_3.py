
def same_vowel_group(w):
  return [w[a] for a in range(len(w)) if set([b for b in w[a] if b in 'aiueo']) == set([a for a in w[0] if a in 'aiueo']) ]

