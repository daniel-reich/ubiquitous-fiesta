
def count_all(txt):
  return {"LETTERS": sum([1 for ch in txt if ch.isalpha()]), "DIGITS": sum([1 for num in txt if num.isdigit()])}

