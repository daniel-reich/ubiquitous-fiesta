
def cap_space(txt):
  ret = ''
  for i in txt:
    if i.isupper():
      ret+=' '+i.lower()
    else:
      ret+=i
  return ret

