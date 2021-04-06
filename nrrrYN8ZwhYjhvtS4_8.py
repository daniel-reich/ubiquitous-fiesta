
def extend_vowels(word, num):
  vowels = "aeiouAEIOU"
  txt = ""
  if type(num) != int or num < 0:
    return "invalid"
  for i in word:
    if i in vowels:
      w = 0
      while w <= num:
        txt += i
        w += 1
    else:
      txt += i
  return txt

