
def split_code(item):
  [a, b] = ["", ""]
  for i in item:
    if i.isdigit():
      b += i
    else:
      a += i
  return [a, int(b)]

