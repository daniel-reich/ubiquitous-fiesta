
def special_reverse_string(txt):
  lst = [i for i in txt[::-1] if i != ' ']
  return ''.join(char if char == ' ' else lst.pop(0).upper() if char.isupper() else lst.pop(0).lower() for char in txt)

