
def fauna_number(txt):
  animals = ["muggercrocodile", "one-hornedrhino", "python", "moth", "monitorlizard", "bengaltiger"]
  txt=''.join(c if c.isalnum() or c=='-' else ' ' for c in txt).split()
  res=[]
  for i in range(len(txt)):
    if txt[i] in animals:
      res+=[(txt[i],txt[i-1])]
  return res

