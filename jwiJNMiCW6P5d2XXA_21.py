
def does_rhyme(s1, s2):
  vowels = "aeuio";
  word1 , word2  = s1.split(" ")[-1].lower()  , s2.split(" ")[-1].lower();
  return all([ ( (vowel in word1) +  (vowel in word2) ) % 2 == 0 for vowel in vowels])

