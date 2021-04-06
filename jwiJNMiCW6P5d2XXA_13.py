
def does_rhyme(txt1, txt2):
  vowels1 = {c.lower() for c in txt1.split()[-1] if c.lower() in "aeiou"}
  vowels2 = {c.lower() for c in txt2.split()[-1] if c.lower() in "aeiou"}
​
  return vowels1 == vowels2

