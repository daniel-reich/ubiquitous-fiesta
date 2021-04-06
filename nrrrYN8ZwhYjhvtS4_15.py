
def extend_vowels(word, num):
  if type(num)!=int or num<0:
    return "invalid"
  return "".join(l*(num+1) if l.lower() in "aeiou" else l for l in word)

