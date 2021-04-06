
def is_palindrome(txt):
  res = txt.lower().replace(" ","")
  res = res.replace("-","")
  res = res.replace(",","")
  res = res.replace("!","")
  return res == res[::-1]

