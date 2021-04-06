
def first_n_vowels(txt, n):
  vowels = "aeiou"
  txt_vowels = "".join(char for char in txt if char in vowels)
  if len(txt_vowels) >= n:
    return txt_vowels[:n]
  else:
    return "invalid"

