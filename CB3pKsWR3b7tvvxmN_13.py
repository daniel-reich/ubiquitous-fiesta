
def is_palindrome(txt):
  punctuation = ' ,!-@#$%^&*()'
  txt = ''.join([x for x in txt if x not in punctuation]).lower()
  return txt[:len(txt)//2]==txt[:-len(txt)//2:-1]

