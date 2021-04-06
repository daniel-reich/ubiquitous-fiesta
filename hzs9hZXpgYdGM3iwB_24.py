
def alternating_caps(txt):
  new_txt=''
  caps=True
  for i in txt:
    if i.isalpha():
      if caps:
        new_txt+=i.upper()
        caps=False
      else:
        new_txt+=i.lower()
        caps=True
    else: new_txt+=i
  return new_txt

