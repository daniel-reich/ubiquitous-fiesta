
def is_authentic_skewer(s):
  alpha= [chr(65+i) for i in range (26)]
  vowels='AEIOUaeiou'
  if '-' not in s or not any(c.isalpha() for c in s) or s[0] in vowels or s[-1] in vowels or not s[0].isalpha():
    return False
  consequtive=max_consequtive=0
  for c in s:
    if c=='-':
      consequtive+=1
      if consequtive > max_consequtive:
        max_consequtive = consequtive
    else:
      consequtive =0
  out=''.join(s.split('-'*max_consequtive))
  if not all(c.isalpha() for c in out) :
    return False
  for i in range (len(out)-1):
    if out[i] in vowels:
      if (out[i+1] in vowels):
        return False
    else:
      if not (out[i+1] in vowels):
        return False
  return True

