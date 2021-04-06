
def first_n_vowels(string, num):
  vowels = "aeiou";
  word_vowels  =  "".join([letter for letter in string if letter in vowels]);
  return word_vowels[0:num] if num <= len(word_vowels) else "invalid";

