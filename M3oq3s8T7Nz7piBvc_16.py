
def even_odd_string(txt):
  evens = ''
  odds = ''
  mylist = []
  for x in txt:
      mylist.append(x)
  for x in range(0, len(txt), 2):
      evens = evens + mylist[x]
  for x in range(1, len(txt), 2):
      odds = odds + mylist[x]
  return evens + " " + odds

