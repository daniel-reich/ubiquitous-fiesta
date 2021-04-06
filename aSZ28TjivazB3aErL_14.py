
import string
def letters_only(s):
  if s == '':
    return False
  else:
    digits = string.digits
    punctuation = string.punctuation
    uppercase = string.ascii_uppercase
    for eachdigit in digits:
      if eachdigit in s:
        return False
    for eachsymbol in punctuation:
      if eachsymbol in s:
        return False
    for eachletter in uppercase:
      if eachletter in s:
        return False
    return True

