
def shift_letters(string, n):                 # Letter shifting
  """ Return the string with all letter shifted to the right n times """
  index, string, new_str = [i for i, x in enumerate(string) if x==" "], [x for x in string if x.isalpha()], []
  n %= len(string)
  new_str = [string[i] for i in range(-n, len(string)-n)]
  for i in index: new_str.insert(i," ")
  return "".join(new_str)

