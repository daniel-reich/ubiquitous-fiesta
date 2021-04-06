
def is_vowel(b):
  vowels = "aeiou"
  if str(b) in vowels:
    return True
  else:
    return False
​
def split(txt):
  vow = ""
  cons = ""
  ans = ""
  for i in txt:
    if is_vowel(i) == True:
      vow += i
    else:
      cons += i
  sorted(vow)
  sorted(cons)
  ans += vow
  ans += cons
  return ans

