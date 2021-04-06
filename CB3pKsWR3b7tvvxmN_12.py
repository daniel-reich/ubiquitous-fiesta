
def is_palindrome(txt):
  og = ''
  result = ''
  for t in txt:
    if t not in '!,.-':
      result=t+result
      og=og+t
  print (og.lower().replace(' ',''))
  print (result.lower().replace(' ',''))
  return og.lower().replace(' ','')==result.lower().replace(' ','')

