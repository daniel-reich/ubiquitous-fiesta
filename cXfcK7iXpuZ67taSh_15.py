
def mystery_func(txt):
  arr = []
  for x in range(len(txt)):
    if (txt[x]).isalpha():
      arr.append(txt[x]*int(txt[x+1]))
  return "".join(arr)

