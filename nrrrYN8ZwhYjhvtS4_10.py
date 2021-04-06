
def extend_vowels(word, num):
  s=''
  if type(num)==int and num>=0:
    for x in word:
      if x.lower() in 'aeiou':
        s+=x*(num+1)
      else:
        s+=x
    return s
  else:
    return "invalid"

