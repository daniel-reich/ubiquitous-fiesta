
def silence_Trump(txt):
  vowels = ['a', 'e', 'i', 'o', 'u']
  lst = list(txt)
  res = []
  for i in lst:
    if i.lower() not in vowels:
      res.append(i)
  result = ''.join(res)
  return result

