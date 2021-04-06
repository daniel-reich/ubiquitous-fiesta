
def is_alphabetically_sorted(sentence):
  s=sentence.strip(".")
  lst=s.split(" ")
  flag=False
  for i in lst:
    if len(i)>=3 and i== "".join(sorted(i.lower())):
      flag=True
      break
  return flag

