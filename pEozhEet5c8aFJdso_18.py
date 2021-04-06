
def all_about_strings(txt):
  array = [len(txt),txt[0], txt[-1], txt[len(txt)//2 - 1:-len(txt)//2 + 1] if len(txt) % 2 == 0 else txt[len(txt)//2:-len(txt)//2 + 1]]
  if txt[1] in txt[2:]:
    array.append("@ index " + str(txt[2:].index(txt[1]) + 2))  
  else:
    array.append("not found")
  return array

