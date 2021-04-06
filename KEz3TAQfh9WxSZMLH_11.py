
def is_letter(char):
  return ord('a') <= ord(char) <= ord('z') or ord('A') <= ord(char) <= ord('Z')
​
def is_number(char):
  return ord('0') <= ord(char) <= ord('9')
​
def count_all(txt):
  dictionary = {}
  dictionary["LETTERS"] = 0
  dictionary["DIGITS"] = 0
  for char in txt:
    dictionary["LETTERS"] += is_letter(char)
    dictionary["DIGITS"] += is_number(char)
  return dictionary

