
def first_n_vowels(txt, n):
  l=[x for x in txt if x in "aeiou"]
  return "".join(l[:n]) if n <=len(l) else "invalid"

