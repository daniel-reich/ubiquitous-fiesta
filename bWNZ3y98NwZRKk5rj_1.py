
def block_player(a, b):
  if a // 3 == b // 3: return (a // 3) * 9 + 3 - a - b
  if a % 3 == b % 3:   return (a % 3) * 3 + 9 - a - b
  return 12 - a - b

