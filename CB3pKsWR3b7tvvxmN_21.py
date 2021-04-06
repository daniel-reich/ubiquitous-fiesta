
def is_palindrome(txt):
  txt1 = ''
  for x in txt:
    if x.isalpha()== True:
      txt1 += x.lower()
  if list(txt1) == list(reversed(txt1)):
    return True
  else:
    return False

