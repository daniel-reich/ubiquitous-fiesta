
def retrieve(txt):
  mylist = []
  vowels = ['a','e','i','o','u']
  words = txt.lower().replace('.','').split()
  for i in range (len(words)):
    if words[i][0] in vowels:
      mylist.append(words[i])
  return mylist

