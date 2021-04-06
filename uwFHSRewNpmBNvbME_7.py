
def same_vowel_group(w):
  def vs(word):
    return {x for x in word if x in "aeiou"}
    
  return [wd for wd in w if vs(wd) <= vs(w[0])]

