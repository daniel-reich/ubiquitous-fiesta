
def is_palindrome(txt):
  txtlist = []
  for char in txt:
    if char.isalpha():
      txtlist.append(char.lower())
  return txtlist == list(reversed(txtlist))

