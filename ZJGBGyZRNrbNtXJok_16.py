
def nearest_vowel(s):
  x= min(abs(ord('a')-ord(s)),abs(ord('e')-ord(s)),abs(ord('i')-ord(s)),abs(ord('o')-ord(s)), abs(ord('u')-ord(s))) 
  if chr(ord(s)-x) in ('aeiou'):
    return chr(ord(s)-x) 
  else:
    return chr(ord(s)+x)

