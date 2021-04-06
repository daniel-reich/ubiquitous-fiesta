
def nearest_vowel(s):
  vowels = "aeiou"
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  for i in range(0, len(alphabet)):
    if alphabet[i] == s:
      s_index = i
  min = len(alphabet)
  closest = ""
  for j in range(0, len(alphabet)):
    if alphabet[j] in vowels:
      if abs(j-s_index) < min:
        min = abs(j-s_index)
        closest = alphabet[j]
  return closest

