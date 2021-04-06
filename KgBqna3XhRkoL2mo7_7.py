
def s_iter(s):
  it = reversed(s)
  while True:
    c = next(it, None)
    if c is None:
      return
    elif c == '#':
      yield int(next(it)) + 10 * int(next(it))
    else:
      yield int(c) 
​
def decrypt(s):
  msg = [chr(96 + x) for x in s_iter(s)]
  return ''.join(reversed(msg))

