
def first_repeat(chars):
  for i in range(len(chars)-1):
    if chars[i] in chars[i+1:]:
      return(chars[i])
  return("-1")

