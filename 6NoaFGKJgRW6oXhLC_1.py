
def sum_of_vowels(sentence):
  txt = sentence.lower()
  return 4 * txt.count('a') + 3 * txt.count('e') + txt.count('i')

