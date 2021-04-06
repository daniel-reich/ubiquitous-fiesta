
def extend_vowels(word, num):
  if num < 0 or type(num) != int:
    return 'invalid'
  vowels = ['a', 'e', 'i', 'o', 'u']
  res_s = ''
  for i in word:
    if i.lower() in vowels:
      res_s += i * num + i
    else:
      res_s += i
  return res_s

