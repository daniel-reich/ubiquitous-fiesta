
def does_rhyme(txt1, txt2):
  lastwords = [txt1.split()[-1].strip(" !.?").lower(), txt2.split()[-1].strip(" !.?").lower()]
  return [lastwords[0].count(vowel) for vowel in "aeiou"] == [lastwords[1].count(vowel) for vowel in "aeiou"]

