
def is_isomorphic(s, t):
  return morph(s) == morph(t)
​
def morph(text):
  result = []
  chars = {}
  cur_val = 0
  for char in text:
    if char not in chars:
      chars[char] = cur_val
      cur_val += 1
    result.append(chars[char])
  return result

