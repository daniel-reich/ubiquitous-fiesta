
def first_non_repeated_character(txt):
  seen_chars = []
  repeated_chars = []
  for char in txt:
    if char in seen_chars:
      repeated_chars.append(char)
    seen_chars.append(char)
    
  for char in txt:
    if char not in repeated_chars:
      return char
  
  return False

