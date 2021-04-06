
def first_repeat(chars):
  for idx, i in enumerate(chars):
    if i in chars[:idx]:
      return i
  return '-1'

