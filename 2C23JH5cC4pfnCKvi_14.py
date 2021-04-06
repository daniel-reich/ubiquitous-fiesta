
def check_flush(table, hand):
  import re
  board = table + hand
  for suits in 'SHDC':
    res = re.findall(suits,''.join(board))
    if len(res) >= 5: return True
  return False

