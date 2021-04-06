
def same_vowel_group(w):
  def calc_val(word):
      vowels = {"a":1, "e":2, "i":4, "o":8, "u":16}
      out = 0
      for letter in word:
          out = out | vowels.get(letter, 0)
          #bitwise or to get unique outputs based on vowels
      return out
​
  out = [w[0],]
  target = calc_val(w[0])
  for word in w[1:]:
      if calc_val(word) == target:
          out.append(word)
  return out

