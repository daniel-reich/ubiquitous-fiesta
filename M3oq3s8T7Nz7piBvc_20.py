
def even_odd_string(txt):
  i = 1
  even =''
  odd =''
  for _ in txt:
    if i % 2 ==0:
      even += txt[i-1]
    else:
      odd += txt[i-1]
    i += 1
  rslt = odd+" "+even
  return rslt

