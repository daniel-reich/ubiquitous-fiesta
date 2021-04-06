
def dashed(txt):
  temp = ""
  vowel = "aeiouAEIOU"
  for i in txt:
    if i in vowel:
      temp += "-{}-".format(i)
    else:
      temp += i
  return temp

