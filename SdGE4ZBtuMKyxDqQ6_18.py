
def first_repeat(chars):
  num_set = set()
  for i in range(len(chars)):
    if chars[i] in num_set:
      return chars[i]
    else:
      num_set.add(chars[i])
  return "-1"

