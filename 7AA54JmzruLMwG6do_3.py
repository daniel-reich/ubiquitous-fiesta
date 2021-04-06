
def is_icecream_sandwich(txt):
  for i,c in enumerate(txt[1:]):
    if txt[i]!=c:
      break
  return len(txt)>2 and set(txt[::-1][:i+1])==set(txt[:i+1]) and len(set(txt[i+1:-i-1]))==1

