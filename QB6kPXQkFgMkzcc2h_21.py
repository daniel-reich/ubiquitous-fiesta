
def remove_abc(txt):
  if txt.count("a") == 0 and txt.count("b") == 0 and txt.count("c") == 0:
    return None
​
  string = ""
  letters = "abc"
  for char in txt:
    if char not in letters:
      string += char
  
  return string

