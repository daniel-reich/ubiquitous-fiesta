
def almost_palindrome(txt):
  txt_rev = txt[::-1]
  different = filter(lambda x: x[0] != x[1], zip(txt, txt_rev))
  return len(list(different)) == 2
  
print(almost_palindrome('meetsysteea'))

