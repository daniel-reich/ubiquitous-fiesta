
def first_n_vowels(txt, n):
  arr = [i for i in txt if i in "aeiouAEIOU"][:n]
  return "".join(arr[:n]) if len(arr) >= n else "invalid"

