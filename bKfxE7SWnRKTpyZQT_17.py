
def replace_vowel(word):
  vowel_nums = {'a':'1', 'e':'2', 'i':'3', 'o':'4', 'u':'5'}
  return ''.join(vowel_nums.get(i, i) for i in word)

