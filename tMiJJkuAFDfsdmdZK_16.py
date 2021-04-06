
def to_snake_case(txt):
  ans = ""
  for letter in txt:
    if letter.isupper():
      ans += '_' + letter.lower()
    else:
      ans += letter
  return ans
​
def to_camel_case(txt):
  # get words
  txt = txt.split('_')
  ans = ""
  ans += txt.pop(0)
  while len(txt) > 0:
    t = txt.pop(0)
    ans += t.capitalize()
  return ans

