
def does_rhyme(txt1, txt2):
  txt1_vowels = [char for char in txt1.lower().split()[-1] if char in 'aeiou']
  txt2_vowels = [char for char in txt2.lower().split()[-1] if char in 'aeiou']
  return txt1_vowels == txt2_vowels

