
def is_icecream_sandwich(txt):
  if len(txt)>2 and len(set(txt))==2:
    if len(txt)%2!=0:
      return txt[:len(txt)//2 +1]==txt[len(txt)//2:][::-1]
    else:
      return txt[:len(txt)//2]==txt[len(txt)//2:][::-1]
  else:
    return False

