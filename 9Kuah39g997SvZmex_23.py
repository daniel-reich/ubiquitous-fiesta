
def common_last_vowel(txt):
  def get_vowel(ch):
    return ch if ch in "aeiou" else None
​
  vowels = [''.join(list(filter(get_vowel,i))) for i in txt.lower().split()]
  c = {i[-1]:sum(1 for j in vowels if j[-1] == i[-1]) for i in vowels}
  return max(c, key=c.get)

