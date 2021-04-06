
def is_palindrome(txt):
  print(txt)
  strippedtxt = ''.join(i.lower() for i in txt if i.isalpha())
  print(strippedtxt+" "+strippedtxt[::-1])
  if (strippedtxt == strippedtxt[::-1]):
    return(True)
  else:
    return(False)

