
def letter_at_position(n):
  if n == 0:
    return 'invalid'
  if isinstance(n, int):
    return chr(int(n) + 96)
  else:
    if str(n)[-2] == '.':
      if str(n)[-1] != '0':
        return 'invalid'
  return chr(int(n) + 96)

