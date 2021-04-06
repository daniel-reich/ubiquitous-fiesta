
from statistics import mode
def common_last_vowel(txt):
  vowels = [[ch for ch in word if ch in "AEIOUaeiou"][-1] for word in txt.split(" ")]
  return mode(vowels).lower()

